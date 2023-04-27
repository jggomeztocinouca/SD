import socket
import os

HOST = 'localhost'
PORT = 1025

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServidor.bind((HOST, PORT))

socketServidor.listen(1)

socketCliente, direccionCliente = socketServidor.accept()

print(f'Conexión entrante del cliente {str(direccionCliente)}')

nombreImagen = socketCliente.recv(1024).decode('utf-8')

if os.path.isfile(nombreImagen):
    socketCliente.send('existe'.encode('utf-8'))
    with open(nombreImagen, 'rb') as imagen:
        socketCliente.sendall(imagen.read())
    print('Imagen enviada')
else:
    socketCliente.send('no existe'.encode('utf-8'))

socketCliente.close()
socketServidor.close()
