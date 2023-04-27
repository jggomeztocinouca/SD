import socket

HOST = 'localhost'
PORT = 1025

def iniciar_chat(socketCliente, direccionCliente):
    print(f'Conexión establecida con el cliente: {direccionCliente}')

    while True:
        mensaje_cliente = socketCliente.recv(1024).decode('utf-8')
        if mensaje_cliente == "desconectar":
            print("El cliente se ha desconectado.")
            break

        print("Cliente:", mensaje_cliente)
        mensaje_servidor = input("Servidor: ")

        if mensaje_servidor == "desconectar":
            socketCliente.send("desconectar".encode('utf-8'))
            break

        socketCliente.send(mensaje_servidor.encode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServidor:
    socketServidor.bind((HOST, PORT))
    print("Servidor corriendo!")
    socketServidor.listen(1)
    socketCliente, direccionCliente = socketServidor.accept()

    with socketCliente:
        iniciar_chat(socketCliente, direccionCliente)

print("Servidor cerrado!")
