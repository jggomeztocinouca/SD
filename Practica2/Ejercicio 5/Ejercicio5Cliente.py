import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para establecer conexión TCP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecemos conexión con el servidor
socketCliente.connect((HOST, PORT))
print("Conexión establecida con el servidor")

# Enviamos el nombre del fichero .jpg al servidor
socketCliente.send("imagen.jpg".encode("utf-8"))

# Comprobamos si la imagen existe
if socketCliente.recv(1024).decode("utf-8") == "Imagen encontrada":
    print("Iniciando descarga de la imagen")
    # Recibimos la imagen
    imagen = open("imagenRecibida.jpg", "wb")
    imagen.write(socketCliente.recv(1024))
    imagen.close()
    print("Imagen recibida")
else:
    print("Imagen no existente en el servidor")

# Cerramos el socket del cliente
socketCliente.close()

