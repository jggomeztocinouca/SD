import json

from bottle import route, run, request, HTTPResponse
import uuid


def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def guardar_usuarios():
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)


def cargar_vehiculos():
    try:
        with open('vehiculos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def guardar_vehiculos():
    with open('vehiculos.json', 'w') as f:
        json.dump(vehiculos, f)


# Mantenemos dos diccionarios en memoria para almacenar la información de los vehículos y usuarios.
usuarios = cargar_usuarios()
vehiculos = cargar_vehiculos()


# Registramos un nuevo usuario
@route('/registrar/usuario', method='POST')
def registrar_usuario():
    id = str(uuid.uuid4())  # Generamos un ID único
    usuarios[id] = {'id': id, 'alquileres': 0}  # Añadimos el nuevo usuario al diccionario
    guardar_usuarios()
    return usuarios[id]  # Devolvemos el nuevo usuario


# Registramos un nuevo vehículo
@route('/registrar/vehiculo', method='POST')
def registrar_vehiculo():
    id = str(uuid.uuid4())  # Generamos un ID único
    datos = request.json  # Obtenemos la marca y modeloo del vehículo desde el cuerpo de la petición
    vehiculos[id] = {'id': id, 'marca': datos['marca'], 'modelo': datos['modelo'], 'alquilado': False,
                     'usuario': None}  # Añadimos el nuevo vehículo al diccionario
    guardar_vehiculos()
    return vehiculos[id]  # Devolvemos el nuevo vehículo


# Alquilamos un vehículo libre
@route('/alquilar/libre/<usuarioid>', method='POST')
def alquilar_vehiculo_libre(usuarioid):
    if usuarioid not in usuarios:
        return HTTPResponse(status=404, body='Usuario no encontrado')
    for id, vehiculo in vehiculos.items():
        if not vehiculo['alquilado']:  # Si encontramos un vehículo libre, lo alquilamos
            vehiculo['alquilado'] = True
            vehiculo['usuario'] = usuarioid
            usuarios[usuarioid]['alquileres'] += 1
            guardar_usuarios()
            guardar_vehiculos()
            return vehiculo
    return HTTPResponse(status=404, body='No hay vehículos libres')


# Alquilamos un vehículo específico
@route('/alquilar/especifico/<usuarioid>/<vehiculoid>', method='POST')
def alquilar_vehiculo_especifico(usuarioid, vehiculoid):
    if usuarioid not in usuarios:
        return HTTPResponse(status=404, body='Usuario no encontrado')
    if vehiculoid not in vehiculos:
        return HTTPResponse(status=404, body='Vehículo no encontrado')
    if vehiculos[vehiculoid]['alquilado']:
        return HTTPResponse(status=400, body='Vehículo ya alquilado')
    vehiculos[vehiculoid]['alquilado'] = True
    vehiculos[vehiculoid]['usuario'] = usuarioid
    usuarios[usuarioid]['alquileres'] += 1
    guardar_usuarios()
    guardar_vehiculos()
    return vehiculos[vehiculoid]


run(host='localhost', port=8080)
