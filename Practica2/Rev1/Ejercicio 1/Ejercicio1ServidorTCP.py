import socket

HOST = 'localhost'
PORT = 1025

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServidor.bind((HOST, PORT))

print('Server up!')

socketServidor.listen(1)

socketCliente, direccionCliente = socketServidor.accept()

print(f'Conexión entrante desde el cliente {str(direccionCliente[0])}:{str(direccionCliente[1])}')

mensaje = socketCliente.recv(1024).decode('utf-8')

print(f'Mensaje del cliente: {mensaje}')

socketCliente.send(input("Introduzca la respuesta a enviar al cliente: ").encode('utf-8'))

socketCliente.close()
socketServidor.close()

print('Server down!')