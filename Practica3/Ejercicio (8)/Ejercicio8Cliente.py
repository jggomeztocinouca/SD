import requests
import json

base_url = 'http://localhost:8080'  # URL base del servidor


# Registrar un aterrizaje
def registrar_aterrizaje():
    registro = input('Introduce la matrícula del avión: ')
    hora_aterrizaje = input('Introduce la hora de aterrizaje (formato "YYYY-MM-DDHH:MM:SS"): ')
    respuesta = requests.post(f'{base_url}/aterrizaje', json={'registro': registro, 'hora_aterrizaje': hora_aterrizaje})
    if respuesta.status_code == 200:
        print('Aterrizaje registrado. ID del avión:', respuesta.json()['id'])
    else:
        print('Error al registrar el aterrizaje:', respuesta.text)


# Registrar un despegue
def registrar_despegue():
    registro = input('Introduce la matrícula del avión: ')
    hora_despegue = input('Introduce la hora de despegue (formato "YYYY-MM-DDHH:MM:SS"): ')
    respuesta = requests.post(f'{base_url}/despegue', json={'registro': registro, 'hora_despegue': hora_despegue})
    if respuesta.status_code == 200:
        print('Despegue registrado')
    else:
        print('Error al registrar el despegue:', respuesta.text)


# Listar todos los aviones del aeropuerto
def list_aviones():
    respuesta = requests.get(f'{base_url}/aviones')
    if respuesta.status_code == 200:
        print('Aviones en el aeropuerto:')
        for avion in respuesta.json()['aviones']:
            print(json.dumps(avion, indent=4))
    else:
        print('Error al listar los aviones:', respuesta.text)


while True:
    print('1. Registrar un aterrizaje')
    print('2. Registrar un despegue')
    print('3. Listar todos los aviones del aeropuerto')
    print('4. Salir')
    opcion = input('Selecciona una opción: ')
    if opcion == '1':
        registrar_aterrizaje()
    elif opcion == '2':
        registrar_despegue()
    elif opcion == '3':
        list_aviones()
    elif opcion == '4':
        break
