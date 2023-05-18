# Importamos los módulos necesarios
import json

from bottle import route, request, HTTPResponse


# Definimos una clase Room para representar las habitaciones del hotel
class Room:
    # El constructor de la clase Room toma un id, número de plazas, equipamiento y estado de ocupación
    def __init__(self, id, num_plazas, equipamiento, ocupada):
        self.id = id
        self.num_plazas = num_plazas
        self.equipamiento = equipamiento
        self.ocupada = ocupada

# Función para guardar las habitaciones en un archivo
def guardar_habitaciones():
    with open('habitaciones.json', 'w') as f:
        json.dump(habitaciones, f)

# Función para cargar las habitaciones de un archivo
def cargar_habitaciones():
    # Intentamos abrir el archivo y cargar el diccionario de habitaciones
    try:
        with open('habitaciones.json', 'rb') as f:
            return json.load(f)
    # Si el archivo no existe, retornamos un diccionario vacío
    except FileNotFoundError:
        return {}

# Cargamos las habitaciones al iniciar el programa
habitaciones = cargar_habitaciones()

# Definimos el endpoint para añadir una nueva habitación con el método POST
@route('/room', method='POST')
def add_room():
    # Obtenemos los datos de la petición
    datos = request.json
    # Verificamos que todos los campos necesarios están presentes
    if 'id' not in datos or 'num_plazas' not in datos or 'equipamiento' not in datos or 'ocupada' not in datos:
        # Si falta algún campo, devolvemos un error 400
        return HTTPResponse(status=400, body='Falta algún parámetro necesario')
    # Creamos una nueva instancia de la clase Room con los datos de la petición
    room = Room(datos['id'], datos['num_plazas'], datos['equipamiento'], datos['ocupada'])
    # Añadimos la nueva habitación al diccionario
    habitaciones[datos['id']] = room
    guardar_habitaciones()
    # Devolvemos un mensaje de éxito
    return HTTPResponse(status=200, body=f'Habitación {datos["id"]} creada correctamente')

# Definimos el endpoint para modificar una habitación existente con el método PUT
@route('/room/<id>', method='PUT')
def modificar_room(id):
    # Obtenemos los datos de la petición
    datos = request.json
    # Verificamos que la habitación exista
    if id not in habitaciones:
        # Si la habitación no existe, devolvemos un error 404
        return HTTPResponse(status=404, body='Habitación no encontrada')
    # Obtenemos la habitación existente
    room = habitaciones[id]
    # Modificamos los campos de la habitación con los datos de la petición
    room.num_plazas = datos.get('num_plazas', room.num_plazas)
    room.equipamiento = datos.get('equipamiento', room.equipamiento)
    room.ocupada = datos.get('ocupada', room.ocupada)
    guardar_habitaciones()
    # Devolvemos un mensaje de éxito
    return HTTPResponse(status=200, body=f'Habitación {id} modificada correctamente')

# Definimos el endpoint para obtener la lista de todas las habitaciones con el método GET
@route('/room', method='GET')
def list_habitaciones():
    # Devolvemos la lista de todas las habitaciones en formato JSON
    return {id: vars(room) for id, room in habitaciones.items()}

# Definimos el endpoint para obtener una habitación específica con el método GET
@route('/room/<id>', method='GET')
def get_room(id):
    # Verificamos que la habitación exista
    if id not in habitaciones:
        # Si la habitación no existe, devolvemos un error 404
        return HTTPResponse(status=404, body='Habitación no encontrada')
    # Obtenemos la habitación existente
    room = habitaciones[id]
    # Devolvemos los datos de la habitación en formato JSON
    return vars(room)

# Definimos el endpoint para eliminar una habitación con el método DELETE
@route('/room/<id>', method='DELETE')
def delete_room(id):
    # Verificamos que la habitación exista
    if id not in habitaciones:
        # Si la habitación no existe, devolvemos un error 404
        return HTTPResponse(status=404, body='Habitación no encontrada')
    # Eliminamos la habitación del diccionario
    del habitaciones[id]
    # Guardamos las habitaciones tras eliminar una
    guardar_habitaciones()
    # Devolvemos un mensaje de éxito
    return HTTPResponse(status=200, body=f'Habitación {id} eliminada correctamente')
