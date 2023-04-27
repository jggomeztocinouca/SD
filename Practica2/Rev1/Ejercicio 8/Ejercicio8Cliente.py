import socket

HOST = 'localhost'
PORT = 1025

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente:
    socketCliente.connect((HOST, PORT))
    print(f'Conexión establecida con el servidor: {HOST}:{PORT}')

    while True:
        mensaje_cliente = input("Cliente: ")
        socketCliente.send(mensaje_cliente.encode('utf-8'))

        if mensaje_cliente == "desconectar":
            break

        mensaje_servidor = socketCliente.recv(1024).decode('utf-8')
        if mensaje_servidor == "desconectar":
            print("El servidor se ha desconectado.")
            break

        print("Servidor:", mensaje_servidor)
