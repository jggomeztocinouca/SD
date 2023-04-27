import os

with open('/etc/passwd', 'r') as archivo:
    for linea in archivo:
        campos = linea.split(':')
        usuario = campos[0]
        directorio_home = campos[5]
        if directorio_home.startswith('/home/'): # Es un usuario del sistema
            print(f"El directorio de inicio de {usuario} es {directorio_home}")