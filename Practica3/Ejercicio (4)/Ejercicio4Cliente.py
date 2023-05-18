import requests  # Importamos el módulo de requests para hacer peticiones HTTP
import json  # Importamos el módulo de json para trabajar con datos en formato JSON

# Definimos la URL base del servidor
base_url = 'http://localhost:8080/personal'

# Definimos una función para añadir un nuevo miembro
def add_miembro():
    miembro = {}  # Creamos un diccionario vacío para almacenar los datos del nuevo miembro
    # Pedimos al usuario que introduzca los datos del nuevo miembro
    miembro['dni'] = input('DNI: ')
    miembro['nombre'] = input('Nombre: ')
    miembro['correo'] = input('Correo: ')
    miembro['departamento'] = input('Departamento: ')
    miembro['categoria'] = input('Categoría (PAS/PDI/becario): ')
    if miembro['categoria'] == 'PDI':  # Si la categoría es PDI
        miembro['asignaturas'] = input('Asignaturas (separadas por comas): ').split(',')  # Pedimos las asignaturas y las guardamos como una lista
    requests.post(base_url, json=miembro)  # Hacemos una petición POST a la URL base para añadir el nuevo miembro, enviando los datos en el cuerpo de la petición

# Definimos una función para obtener toda la lista de personal
def get_all():
    respuesta = requests.get(base_url)  # Hacemos una petición GET a la URL base para obtener toda la lista de personal
    print(json.dumps(respuesta.json(), indent=2))  # Imprimimos la respuesta, formateándola para que sea más legible

# Definimos una función para obtener un miembro por DNI
def get_miembro():
    dni = input('DNI: ')  # Pedimos al usuario que introduzca el DNI del miembro que quiere obtener
    respuesta = requests.get(f'{base_url}/{dni}')  # Hacemos una petición GET a la URL correspondiente para obtener el miembro
    print(json.dumps(respuesta.json(), indent=2))  # Imprimimos la respuesta, formateándola para que sea más legible

# Definimos una función para modificar un miembro
def modify_miembro():
    dni = input('DNI: ')  # Pedimos al usuario que introduzca el DNI del miembro que quiere modificar
    miembro = {}  # Creamos un diccionario vacío para almacenar los nuevos datos del miembro
    # Pedimos al usuario que introduzca los nuevos datos del miembro
    miembro['nombre'] = input('Nombre: ')
    miembro['correo'] = input('Correo: ')
    miembro['departamento'] = input('Departamento: ')
    miembro['categoria'] = input('Categoría (PAS/PDI/becario): ')
    if miembro['categoria'] == 'PDI':  # Si la nueva categoría es PDI
        miembro['asignaturas'] = input('Asignaturas (separadas por comas): ').split(',')  # Pedimos las nuevas asignaturas y las guardamos como una lista
    requests.put(f'{base_url}/{dni}', json=miembro)  # Hacemos una petición PUT a la URL correspondiente para modificar el miembro, enviando los nuevos datos en el cuerpo de la petición

# Definimos una función para eliminar un miembro
def delete_miembro():
    dni = input('DNI: ')  # Pedimos al usuario que introduzca el DNI del miembro que quiere eliminar
    requests.delete(f'{base_url}/{dni}')  # Hacemos una petición DELETE a la URL correspondiente para eliminar el miembro

while True:  # Iniciamos un bucle infinito
    # Imprimimos el menú de opciones
    print('1. Añadir miembro')
    print('2. Obtener todos los miembros')
    print('3. Obtener miembro por DNI')
    print('4. Modificar miembro')
    print('5. Eliminar miembro')
    print('6. Salir')
    opcion = input('Seleccione una opción: ')  # Pedimos al usuario que seleccione una opción
    # Según la opción seleccionada, llamamos a la función correspondiente
    if opcion == '1':
        add_miembro()
    elif opcion == '2':
        get_all()
    elif opcion == '3':
        get_miembro()
    elif opcion == '4':
        modify_miembro()
    elif opcion == '5':
        delete_miembro()
    elif opcion == '6':
        break  # Si la opción es 6, salimos del bucle infinito
