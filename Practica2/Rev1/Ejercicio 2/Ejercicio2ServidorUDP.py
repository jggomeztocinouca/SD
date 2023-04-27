import socket
import os

HOST = 'localhost'
PORT = 1025

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketServidor.bind((HOST, PORT))

print("Server up!")

nombreFichero, direccionCliente = socketServidor.recvfrom(1024)

nombreFichero = nombreFichero.decode('utf-8')

solicitudAprobada = True

if os.path.isfile(nombreFichero):
    solicitudAprobada = False
    socketServidor.sendto(f'El archivo con nombre {nombreFichero} ya existe en el servidor. ¿Desea sobreescribirlo?'.encode('utf-8'),direccionCliente)
    respuesta = socketServidor.recv(1024).decode('utf-8')
    if respuesta == 's' or respuesta == 'S':
        solicitudAprobada = True
else:
    socketServidor.sendto('ok'.encode('utf-8'),direccionCliente)

if solicitudAprobada:
    size = int(socketServidor.recv(1024).decode('utf-8'))
    with open('copia_' + nombreFichero, 'wb') as fichero:
        while size > 0:
            datos = socketServidor.recv(4096)
            fichero.write(datos)
            size -= len(datos)
    socketServidor.sendto('Archivo recibido'.encode('utf-8'),direccionCliente)

socketServidor.close()
print('Server down!')
