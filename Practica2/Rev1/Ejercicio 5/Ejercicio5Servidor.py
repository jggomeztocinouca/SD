import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para establecer conexión TCP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket con la dirección y puerto
socketServidor.bind((HOST, PORT))

print("Server running!")

# Ponemos al servidor a la escucha de peticiones de, como máximo, 1 cliente
socketServidor.listen(1)

# Aceptamos la conexión del cliente y creamos un nuevo socket para comunicarnos con él
socketCliente, direccionCliente = socketServidor.accept()
print("Conexión entrante de: ", direccionCliente)

# Recibimos el nombre del fichero .jpg del cliente
nombreFichero = socketCliente.recv(1024).decode("utf-8")
socketCliente.send("Petición recibida".encode("utf-8"))

# Enviamos la imagen o el mensaje de error al cliente
try:
    imagen = open(nombreFichero, "rb")
    socketCliente.send("Imagen encontrada".encode("utf-8"))
    socketCliente.sendall(imagen.read())
    imagen.close()
    print("Imagen enviada")
except IOError:
    socketCliente.send("Imagen no existente".encode("utf-8"))

# Cerramos el socket del cliente
socketCliente.close()

# Cerramos el socket del servidor
socketServidor.close()

print("Server stopped!")