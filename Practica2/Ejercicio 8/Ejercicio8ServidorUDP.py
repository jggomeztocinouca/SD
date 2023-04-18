import socket

HOST = 'localhost'
PORT = 1025

def iniciar_chat(socketServidor):
    while True:
        mensaje_cliente, direccionCliente = socketServidor.recvfrom(1024)
        mensaje_cliente = mensaje_cliente.decode('utf-8')
        if mensaje_cliente == "desconectar":
            print("El cliente se ha desconectado.")
            break

        print(f"Cliente: {mensaje_cliente}")
        mensaje_servidor = input("Servidor: ")

        if mensaje_servidor == "desconectar":
            socketServidor.sendto("desconectar".encode('utf-8'), direccionCliente)
            break

        socketServidor.sendto(mensaje_servidor.encode('utf-8'), direccionCliente)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socketServidor:
    socketServidor.bind((HOST, PORT))
    print("Servidor corriendo!")
    iniciar_chat(socketServidor)

print("Servidor cerrado!")
