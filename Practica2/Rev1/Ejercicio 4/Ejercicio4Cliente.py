import socket

HOST = 'localhost'
PORT = 1025

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketCliente.sendto(''.encode('utf-8'), (HOST, PORT))

respuesta = socketCliente.recv(1024).decode('utf-8')
print(f'Server says: {respuesta}')

socketCliente.sendto(input('Introduzca su nombre: ').encode('utf-8'), (HOST, PORT))

respuesta = socketCliente.recv(1024).decode('utf-8')
print(f'Server says: {respuesta}')

consulta = ''
while consulta != 'exit':
    consulta = input("Introduzca una nueva consulta: ")
    socketCliente.sendto(consulta.encode('utf-8'), (HOST, PORT))

    respuesta = socketCliente.recv(1024).decode('utf-8')
    print(f'Server says: {respuesta}')

    respuesta = socketCliente.recv(1024).decode('utf-8')
    print(f'Server says: {respuesta}')

socketCliente.close()
