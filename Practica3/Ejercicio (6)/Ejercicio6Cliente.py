import requests
import json

base_url = 'http://localhost:8080'  # URL base del servidor

# Registramos un nuevo usuario
def register_user():
    response = requests.post(f'{base_url}/register/user')
    print(f'Usuario registrado: {response.json()}')

# Registramos un nuevo vehículo
def register_vehicle():
    brand = input('Introduce la marca del vehículo: ')
    model = input('Introduce el modelo del vehículo: ')
    response = requests.post(f'{base_url}/register/vehicle', json={'brand': brand, 'model': model})
    print(f'Vehículo registrado: {response.json()}')

# Alquilamos un vehículo libre
def rent_free_vehicle():
    userid = input('Introduce el ID del usuario: ')
    response = requests.post(f'{base_url}/rent/free/{userid}')
    if response.status_code == 200:
        print(f'Vehículo alquilado: {response.json()}')
    else:
        print('Error:', response.text)

# Alquilamos un vehículo específico
def rent_specific_vehicle():
    userid = input('Introduce el ID del usuario: ')
    vehicleid = input('Introduce el ID del vehículo: ')
    response = requests.post(f'{base_url}/rent/specific/{userid}/{vehicleid}')
    if response.status_code == 200:
        print(f'Vehículo alquilado: {response.json()}')
    else:
        print('Error:', response.text)

# Menú principal
while True:
    print('1. Registrar usuario')
    print('2. Registrar vehículo')
    print('3. Alquilar vehículo libre')
    print('4. Alquilar vehículo específico')
    print('5. Salir')
    option = input('Selecciona una opción: ')
    if option == '1':
        register_user()
    elif option == '2':
        register_vehicle()
    elif option == '3':
        rent_free_vehicle()
    elif option == '4':
        rent_specific_vehicle()
    elif option == '5':
        break
