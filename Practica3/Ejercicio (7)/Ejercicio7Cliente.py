import requests

base_url = 'http://localhost:8080'  # URL base del servidor


# Reservar una pista
def reserve():
    pista = int(input('Introduce el número de la pista: '))
    inicio_hora = int(input('Introduce la hora de inicio: '))
    fini_hora = int(input('Introduce la hora de fin: '))
    jugador = input('Introduce el nombre del jugador: ')
    respuesta = requests.post(f'{base_url}/reservar',
                              json={'pista': pista, 'inicio_hora': inicio_hora, 'fini_hora': fini_hora,
                                    'jugador': jugador})
    if respuesta.status_code == 200:
        print('Reserva realizada. Identificador de la reserva:', respuesta.json()['id'])
    else:
        print('Error al realizar la reserva:', respuesta.text)


# Cancelar una reserva
def cancel():
    id = input('Introduce el identificador de la reserva: ')
    respuesta = requests.delete(f'{base_url}/cancelar/{id}')
    if respuesta.status_code == 200:
        print('Reserva cancelada')
    else:
        print('Error al cancelar la reserva:', respuesta.text)


# Mostrar las reservas de una pista
def show():
    pista = input('Introduce el número de la pista: ')
    respuesta = requests.get(f'{base_url}/mostrar/{pista}')
    if respuesta.status_code == 200:
        print('Reservas de la pista:')
        for reserva in respuesta.json()['reservas']:
            print(f"{reserva['inicio_hora']} a {reserva['fini_hora']}: reservada por {reserva['jugador']}")
    else:
        print('Error al obtener las reservas de la pista:', respuesta.text)


while True:
    print('1. Reservar una pista')
    print('2. Cancelar una reserva')
    print('3. Mostrar las reservas de una pista')
    print('4. Salir')
    opcion = input('Selecciona una opción: ')
    if opcion == '1':
        reserve()
    elif opcion == '2':
        cancel()
    elif opcion == '3':
        show()
    elif opcion == '4':
        break
