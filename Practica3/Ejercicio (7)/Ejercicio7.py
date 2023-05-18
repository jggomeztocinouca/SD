import json

from bottle import route, run, request, HTTPResponse
import uuid

def cargar_reservas():
    try:
        with open('reservas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def guardar_reservas():
    with open('reservas.json', 'w') as f:
        json.dump(reservas, f)

# Mantenemos un diccionario en memoria para almacenar la información de las reservas.
reservas = cargar_reservas()

# Reservar una pista
@route('/reservar', method='POST')
def reserve():
    datos = request.json  # Obtenemos la información de la reserva del cuerpo de la petición
    for reserva in reservas.values():
        # Verificamos si la pista ya está reservada para esa franja horaria
        if reserva['pista'] == datos['pista'] and (reserva['inicio_hora'] <= datos['inicio_hora'] < reserva['fin_hora'] or reserva['inicio_hora'] < datos['fin_hora'] <= reserva['fin_hora']):
            return HTTPResponse(status=400, body='La pista ya está reservada para esa franja horaria')
    id = str(uuid.uuid4())  # Generamos un ID único
    reservas[id] = {'id': id, 'pista': datos['pista'], 'inicio_hora': datos['inicio_hora'], 'fin_hora': datos['fin_hora'], 'player': datos['player']}  # Añadimos la nueva reserva al diccionario
    guardar_reservas()
    return reservas[id]  # Devolvemos la nueva reserva

# Cancelar una reserva
@route('/cancelar/<id>', method='DELETE')
def cancel(id):
    if id not in reservas:
        return HTTPResponse(status=404, body='No existe ninguna reserva con ese identificador')
    del reservas[id]  # Eliminamos la reserva del diccionario
    guardar_reservas()
    return {'estado': 'éxito'}

# Mostrar las reservas de una pista
@route('/mostrar/<pista>', method='GET')
def show(pista):
    pista_reservas = [reserva for reserva in reservas.values() if reserva['pista'] == int(pista)]  # Filtramos las reservas de la pista especificada
    pista_reservas.sort(key=lambda x: x['inicio_hora'])  # Ordenamos las reservas por la hora de inicio
    return {'reservas': pista_reservas}

run(host='localhost', port=8080)
