import socket

HOST = 'localhost'
PORT = 1025

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketServidor.bind((HOST, PORT))

print('Server up!')

mensaje, direccionCliente = socketServidor.recvfrom(1024)

print(f'Conexión entrante desde el cliente {str(direccionCliente)}')

socketServidor.sendto('¡Bienvenido! ¿Cuál es su nombre para que pueda dirigirme a usted?'.encode('utf-8'), direccionCliente)

nombreCliente = socketServidor.recv(1024).decode('utf-8')

consulta = ''

while consulta != 'exit':
    socketServidor.sendto(f'{nombreCliente}, ¿en qué puedo ayudarte?'.encode('utf-8'), direccionCliente)

    consulta = socketServidor.recv(1024).decode('utf-8')

    if consulta == 'exit':
        socketServidor.sendto('¡Adiós!'.encode('utf-8'), direccionCliente)
    else:
        socketServidor.sendto('Debe ponerse en contacto con el servicio de atención de dudas cuya dirección es '
                              'dudas@ejemplo.com'.encode('utf-8'), direccionCliente)


socketServidor.close()
print('Server down!')

