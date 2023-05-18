import json
import uuid

from bottle import route, run, request, HTTPResponse

def cargar_aviones():
    try:
        with open('aviones.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def guardar_aviones():
    with open('aviones.json', 'w') as f:
        json.dump(aviones, f)

# Mantenemos un diccionario en memoria para almacenar la información de los aviones.
aviones = cargar_aviones()


# Función para obtener el número de pista con menor frecuencia de uso
def get_pista():
    pistas = [0, 0]  # Número de usos de las pistas 10 y 30
    for avion in aviones.values():
        if avion['aterrizaje_pista'] == 10:
            pistas[0] += 1
        elif avion['aterrizaje_pista'] == 30:
            pistas[1] += 1
        if avion['despegue_pista'] == 10:
            pistas[0] += 1
        elif avion['despegue_pista'] == 30:
            pistas[1] += 1
    return 10 if pistas[0] < pistas[1] else 30

# Registro de aterrizaje
@route('/aterrizaje', method='POST')
def aterrizaje():
    datos = request.json
    id = str(uuid.uuid4())  # Generamos un ID único
    aviones[id] = {
        'id': id,
        'registration': datos['registration'],
        'aterrizaje_hora': datos['aterrizaje_hora'],
        'aterrizaje_pista': get_pista(),
        'despegue_hora': None,
        'despegue_pista': None,
    }
    guardar_aviones()
    return aviones[id]

# Registro de despegue
@route('/despegue', method='POST')
def despegue():
    datos = request.json
    for avion in aviones.values():
        if avion['registration'] == datos['registration']:
            if avion['despegue_hora'] is None:
                avion['despegue_hora'] = datos['despegue_hora']
                avion['despegue_pista'] = get_pista()
                guardar_aviones()
                return avion
            else:
                return HTTPResponse(status=400, body='El avión ya ha despegado')
    return HTTPResponse(status=404, body='Avión no encontrado')

# Listado de todos los aviones del aeropuerto
@route('/aviones', method='GET')
def list_aviones():
    return {'aviones': list(aviones.values())}

run(host='localhost', port=8080)
