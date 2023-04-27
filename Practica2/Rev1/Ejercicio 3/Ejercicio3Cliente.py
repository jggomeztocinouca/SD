import socket
import os

HOST = 'localhost'
PORT = 1025

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nombreArchivo = input('Introduzca el nombre del archivo a enviar para su inversión: ')

while not os.path.isfile(nombreArchivo):
    nombreArchivo = input('El archivo no existe. Introduzca el nombre del archivo a enviar para su inversión: ')

socketCliente.sendto(nombreArchivo.encode('utf-8'), (HOST, PORT))

with open(nombreArchivo, 'r') as archivo:
    socketCliente.sendto(archivo.read().encode('utf-8'), (HOST, PORT))

print('Archivo enviado.')

size = int(socketCliente.recv(1024).decode('utf-8'))

with open('inverted_' + nombreArchivo, 'w') as archivo:
    contenido = socketCliente.recv(size).decode('utf-8')
    archivo.write(contenido)

print('Archivo recibido!')
print(f'Contenido invertido: {contenido}. Tamaño: {size} bytes')

socketCliente.close()
