import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el socket
socketCliente.connect((HOST, PORT))

# Imprimimos el mensaje de bienvenida
print("Server says: " + socketCliente.recv(1024).decode("utf-8"))

# Enviamos el mensaje
socketCliente.send(input().encode("utf-8"))

consulta = ""

# Imprimimos el mensaje
while consulta != "exit":
    print("Server says: " + socketCliente.recv(1024).decode("utf-8"))
    consulta = input()
    socketCliente.send(consulta.encode("utf-8"))

# Imprimimos el mensaje de despedida
print("Server says: " + socketCliente.recv(1024).decode("utf-8"))

# Cerramos el socket
socketCliente.close()
