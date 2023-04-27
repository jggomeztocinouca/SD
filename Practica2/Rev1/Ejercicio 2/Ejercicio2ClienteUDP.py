import socket
import os

HOST = 'localhost'
PORT = 1025

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nombreArchivo = input("Introduzca el nombre del fichero a enviar: ")

while not os.path.isfile(nombreArchivo) or type(nombreArchivo) is not str:
    nombreArchivo= input('El archivo no existe. Introduzca un nombre válido: ')

socketCliente.sendto(nombreArchivo.encode('utf-8'), (HOST, PORT))

respuesta = socketCliente.recv(1024).decode('utf-8')

enviarArchivo = True

if respuesta != 'ok':
    print(f'Server says: {respuesta}')
    opcion = input("Introduzca la opción: ")
    socketCliente.sendto(opcion.encode('utf-8'), (HOST, PORT))
    if opcion == 'N' or opcion == 'n':
        enviarArchivo = False

if enviarArchivo:
    socketCliente.sendto(str(os.path.getsize(nombreArchivo)).encode('utf-8'), (HOST, PORT))
    with open(nombreArchivo, 'rb') as fichero:
        chunk = fichero.read(4096)
        while chunk:
            socketCliente.sendto(chunk, (HOST, PORT))
            chunk = fichero.read(4096)
