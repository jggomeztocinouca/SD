import requests
import json

base_url = 'http://localhost:8080'  # URL base del servidor


# Función para registrar un usuario
def register():
    user = {'username': input('Nombre de usuario: '),
            'password': input('Contraseña: '),
            'email': input('Correo electrónico: '),
            'name': input('Nombre: '),
            'surname': input('Apellidos: ')}
    response = requests.post(f'{base_url}/register', json=user)
    print(response.json())


# Función para activar una cuenta
def activate():
    data = {'username': input('Nombre de usuario: '),
            'email': input('Correo electrónico: ')}
    response = requests.post(f'{base_url}/activate', json=data)
    print(response.json())


# Función para buscar usuarios
def search():
    data = {'query': input('Consulta: ')}
    response = requests.post(f'{base_url}/search', json=data)
    print(json.dumps(response.json(), indent=2))


while True:
    print('1. Registrar usuario')
    print('2. Activar cuenta')
    print('3. Buscar usuarios')
    print('4. Salir')
    option = input('Seleccione una opción: ')
    if option == '1':
        register()
    elif option == '2':
        activate()
    elif option == '3':
        search()
    elif option == '4':
        break
