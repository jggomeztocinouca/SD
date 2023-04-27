import socket
import os

HOST = 'localhost'
PORT = 1025

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((HOST, PORT))

nombreArchivo = input("Introduzca el nombre del fichero a enviar: ")

while not os.path.isfile(nombreArchivo) or type(nombreArchivo) is not str:
    nombreArchivo = input('El archivo no existe. Introduzca un nombre válido: ')

socketCliente.send(nombreArchivo.encode('utf-8'))

respuesta = socketCliente.recv(1024).decode('utf-8')

enviarArchivo = True

if respuesta != 'ok':
    print(f'Server says: {respuesta}')
    opcion = input("Introduzca la opción: ")
    socketCliente.send(opcion.encode('utf-8'))
    if opcion == 'N' or opcion == 'n':
        enviarArchivo = False

if enviarArchivo:
    socketCliente.send(str(os.path.getsize(nombreArchivo)).encode('utf-8'))
    with open(nombreArchivo, 'rb') as fichero:
        socketCliente.sendall(fichero.read())
