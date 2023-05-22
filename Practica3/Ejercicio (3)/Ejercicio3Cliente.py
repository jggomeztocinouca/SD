# Importamos el módulo requests para hacer las solicitudes HTTP
import requests

# Dirección del Servidor
API_URL = 'http://localhost:8080/room'


def add_room():
    # Solicitamos los datos de la nueva habitación al usuario
    id = input("Introduzca el id de la habitación: ")
    num_plazas = int(input("Introduzca el número de plazas: "))
    equipamiento = input("Introduzca el equipamiento (separado por comas): ").split(',')
    ocupada = input("¿Está ocupada la habitación? (s/n): ").lower() == 's'
    # Hacemos una solicitud POST a la API para añadir la habitación
    respuesta = requests.post(API_URL, json={
        'id': id,
        'num_plazas': num_plazas,
        'equipamiento': equipamiento,
        'ocupada': ocupada
    })
    # Imprimimos la respuesta de la API
    print('respuesta:', respuesta.json())


def list_rooms():
    # Hacemos una solicitud GET a la API para obtener la lista de habitaciones
    respuesta = requests.get(API_URL)
    # Imprimimos la lista de habitaciones
    print('Habitaciones:', respuesta.json())


# Función principal que presenta un menú al usuario
def main():
    while True:
        # Imprimimos el menú
        print("""
        1. Añadir habitación
        2. Listar habitaciones
        3. Salir
        """)
        # Solicitamos la elección del usuario
        opcion = input("Elija una opción: ")
        # Ejecutamos la opción correspondiente
        if opcion == '1':
            add_room()
        elif opcion == '2':
            list_rooms()
        elif opcion == '3':
            break


if __name__ == '__main__':
    main()
