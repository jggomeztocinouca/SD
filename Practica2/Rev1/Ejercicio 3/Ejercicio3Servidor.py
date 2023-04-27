import socket

HOST = 'localhost'
PORT = 1025

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketServidor.bind((HOST, PORT))

print('Server up!')

mensaje, direccionCliente = socketServidor.recvfrom(1024)

print(f'Conexión entrante desde el cliente {str(direccionCliente)}')

mensaje = mensaje.decode('utf-8')

cadenaInvertida = socketServidor.recv(4096).decode('utf-8')

print('Archivo recibido')

print(f'Cadena original: {cadenaInvertida}')

cadenaInvertida = cadenaInvertida[::-1]

print(f'Cadena invertida: {cadenaInvertida}')

socketServidor.sendto(str(len(cadenaInvertida)).encode('utf-8'), direccionCliente)

socketServidor.sendto(cadenaInvertida.encode('utf-8'), direccionCliente)

print('Tamaño y cadena invertida enviados')

socketServidor.close()

print('Server down!')



