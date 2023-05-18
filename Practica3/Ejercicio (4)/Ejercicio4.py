import json  # Importamos el módulo de json para trabajar con datos en formato JSON
from bottle import request, HTTPResponse, route, run  # Importamos los elementos necesarios del módulo de bottle

# Esta función permite cargar la información de personal de un archivo
def cargar_personal():
    try:
        with open('personal.json', 'r') as f:  # Intentamos abrir el archivo personal.json en modo de lectura
            return json.load(f)  # Devolvemos los datos cargados del archivo
    except FileNotFoundError:  # En caso de que el archivo no exista
        return {}  # Devolvemos un diccionario vacío

# Esta función permite guardar la información de personal en un archivo
def guardar_personal():
    with open('personal.json', 'w') as f:  # Abrimos el archivo personal.json en modo de escritura
        json.dump(personal, f)  # Guardamos los datos de personal en el archivo

personal = cargar_personal()  # Iniciamos el diccionario de personal con la función load_personal()

# Definimos el endpoint para obtener la lista de todo el personal
@route('/personal', method='GET')
def get_all():
    return personal  # Devolvemos todo el personal

# Definimos el endpoint para obtener un miembro por DNI
@route('/personal/<dni>', method='GET')
def get_miembro(dni):  # Recibimos el DNI como parámetro en la URL
    if dni not in personal:  # Si el DNI no está en personal
        return HTTPResponse(status=404, body='Miembro no encontrado')  # Devolvemos un error 404
    return personal[dni]  # Si el DNI está en personal, devolvemos los datos del miembro correspondiente

# Definimos el endpoint para añadir un miembro nuevo
@route('/personal', method='POST')
def add_miembro():
    nuevo_miembro = request.json  # Obtenemos los datos del nuevo miembro del cuerpo de la petición
    if 'dni' not in nuevo_miembro:  # Si no se incluyó el DNI en los datos
        return HTTPResponse(status=400, body='Falta el DNI')  # Devolvemos un error 400
    if nuevo_miembro['dni'] in personal:  # Si el DNI ya existe en personal
        return HTTPResponse(status=400, body='El DNI ya existe')  # Devolvemos un error 400
    if 'asignaturas' in nuevo_miembro and nuevo_miembro['categoria'] != 'PDI':  # Si se incluyeron asignaturas y la categoría no es PDI
        return HTTPResponse(status=400, body='Solo los miembros PDI pueden tener asignaturas')  # Devolvemos un error 400
    personal[nuevo_miembro['dni']] = nuevo_miembro  # Agregamos el nuevo miembro a personal
    guardar_personal()  # Guardamos los datos de personal en el archivo
    return nuevo_miembro  # Devolvemos los datos del nuevo miembro

# Definimos el endpoint para modificar los datos de un miembro
@route('/personal/<dni>', method='PUT')
def modificar_miembro(dni):  # Recibimos el DNI como parámetro en la URL
    if dni not in personal:  # Si el DNI no está en personal
        return HTTPResponse(status=404, body='Miembro no encontrado')  # Devolvemos un error 404
    miembro = request.json  # Obtenemos los nuevos datos del miembro del cuerpo de la petición
    # Para cada uno de los atributos que podemos modificar, comprobamos si se incluyeron en los nuevos datos y en caso afirmativo los actualizamos
    if 'nombre' in miembro:
        personal[dni]['nombre'] = miembro['nombre']
    if 'correo' in miembro:
        personal[dni]['correo'] = miembro['correo']
    if 'departamento' in miembro:
        personal[dni]['departamento'] = miembro['departamento']
    if 'categoria' in miembro:
        personal[dni]['categoria'] = miembro['categoria']
    if 'asignaturas' in miembro:  # Si se incluyeron asignaturas
        if personal[dni]['categoria'] != 'PDI':  # Y la categoría no es PDI
            return HTTPResponse(status=400, body='Solo los miembros PDI pueden tener asignaturas')  # Devolvemos un error 400
        personal[dni]['asignaturas'] = miembro['asignaturas']  # Si la categoría es PDI, actualizamos las asignaturas
    guardar_personal()  # Guardamos los datos de personal en el archivo
    return personal[dni]  # Devolvemos los datos del miembro modificado

# Definimos el endpoint para eliminar un miembro
@route('/personal/<dni>', method='DELETE')
def delete_miembro(dni):  # Recibimos el DNI como parámetro en la URL
    if dni not in personal:  # Si el DNI no está en personal
        return HTTPResponse(status=404, body='Miembro no encontrado')  # Devolvemos un error 404
    del personal[dni]  # Si el DNI está en personal, eliminamos el miembro correspondiente
    guardar_personal()  # Guardamos los datos de personal en el archivo
    return HTTPResponse(status=200, body='Miembro eliminado')  # Devolvemos una respuesta con estado 200 y un mensaje indicando que el miembro fue eliminado

run(host='localhost', port=8080)  # Iniciamos el servidor en el puerto 8080 de localhost
