import socket

HOST = 'localhost'
PORT = 1025

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketCliente.sendto(input("Introduzca el mensaje a enviar al servidor: ").encode('utf-8'), (HOST, PORT))

respuesta, direccionServidor = socketCliente.recvfrom(1024)

respuesta = respuesta.decode('utf-8')

print(f'Respuesta del servidor: {respuesta}')

socketCliente.close()
