import socket

HOST = 'localhost'
PORT = 1025

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketServidor.bind((HOST, PORT))

print('Server running!')

mensaje, direccionCliente = socketServidor.recvfrom(1024)

mensaje = mensaje.decode('utf-8')

print(f'Mensaje del cliente: {mensaje}')

socketServidor.sendto(input("Introduzca la respuesta a enviar al cliente: ").encode('utf-8'),direccionCliente)

socketServidor.close()

print('Server closed!')

