import json

from bottle import request, HTTPResponse, run, route


def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def guardar_usuarios():
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)


usuarios = cargar_usuarios()  # Iniciamos el diccionario de usuarios


# Definimos el endpoint para el registro de usuarios
@route('/register', method='POST')
def register():
    usuario = request.json  # Obtenemos la información del usuario del cuerpo de la solicitud
    nombre_usuario = usuario.get('nombre_usuario')  # Obtenemos el nombre de usuario
    email = usuario.get('email')  # Obtenemos el correo electrónico

    # Verificamos si el nombre de usuario o el correo electrónico ya están registrados
    for user in usuarios.values():
        if user['nombre_usuario'] == nombre_usuario or user['email'] == email:
            return HTTPResponse(status=400, body='Usuario o correo ya existen')

    usuario['activado'] = False  # Establecemos la cuenta como no activada
    usuarios[nombre_usuario] = usuario  # Agregamos el usuario al diccionario
    guardar_usuarios()
    return usuario  # Devolvemos la información del usuario registrado


# Definimos el endpoint para la activación de la cuenta
@route('/activate', method='POST')
def activate():
    datos = request.json  # Obtenemos los datos de la solicitud
    nombre_usuario = datos.get('nombre_usuario')  # Obtenemos el nombre de usuario
    email = datos.get('email')  # Obtenemos el correo electrónico

    # Buscamos al usuario en la base de datos
    for user in usuarios.values():
        if user['nombre_usuario'] == nombre_usuario or user['email'] == email:
            if user['activado']:
                return HTTPResponse(status=400, body='La cuenta ya está activada')
            else:
                user['activado'] = True  # Activamos la cuenta
                guardar_usuarios()
                return user  # Devolvemos la información del usuario activado

    return HTTPResponse(status=404, body='Usuario no encontrado')  # El usuario no se encontró


# Definimos el endpoint para la búsqueda de usuarios
@route('/search', method='POST')
def search():
    datos = request.json  # Obtenemos los datos de la solicitud
    busqueda = datos.get('busqueda')  # Obtenemos la cadena de búsqueda

    # Buscamos a todos los usuarios que coincidan con la consulta
    coincidentes_usuarios = [user for user in usuarios.values() if
                             busqueda in user['nombre_usuario'] or busqueda in user['email']]
    return {'usuarios': coincidentes_usuarios}  # Devolvemos los usuarios que coinciden


run(host='localhost', port=8080)
