import socket

HOST = 'localhost'
PORT = 1025

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((HOST, PORT))

socketCliente.send(input("Introduzca el mensaje a enviar al servidor: ").encode('utf-8'))

respuesta = socketCliente.recv(1024).decode('utf-8')

print(f'Respuesta del servidor: {respuesta}')

socketCliente.close()