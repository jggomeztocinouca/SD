import socket

HOST = 'localhost'
PORT = 1025

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socketCliente:
    print(f'Conexión establecida con el servidor: {HOST}:{PORT}')

    while True:
        mensaje_cliente = input("Cliente: ")
        socketCliente.sendto(mensaje_cliente.encode('utf-8'), (HOST, PORT))

        if mensaje_cliente == "desconectar":
            break

        mensaje_servidor, _ = socketCliente.recvfrom(1024)
        mensaje_servidor = mensaje_servidor.decode('utf-8')

        if mensaje_servidor == "desconectar":
            print("El servidor se ha desconectado.")
            break

        print(f"Servidor: {mensaje_servidor}")
