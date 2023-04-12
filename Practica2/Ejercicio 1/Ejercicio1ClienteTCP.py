import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para establecer la conexión TCP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nos conectamos al servidor mediante la dirección y puerto del host al servidor
socketCliente.connect((HOST,PORT))

# Envíamos el mensaje al servidor
socketCliente.send("Hola Servidor, soy el Cliente".encode("utf-8"))

# Recibimos el mensaje del servidor
print(socketCliente.recv(1024).decode("utf-8"))

# Cerramos el socket
socketCliente.close()

