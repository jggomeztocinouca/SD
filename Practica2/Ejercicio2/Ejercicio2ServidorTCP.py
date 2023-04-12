import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para la conexión UDP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociamos el socket a la dirección y puerto
socketServidor.bind((HOST, PORT))

print("Server running!")

# Ponemos el servidor a la escucha de, como máximo, 1 petición
socketServidor.listen(1)

# Aceptamos la conexión del cliente
socketCliente, direccionCliente = socketServidor.accept()

# Recibimos el nombre del archivo PDF que queremos obtener
nombreArchivo = socketCliente.recv(1024) # Usamos recv porque tenemos un socket propio para comunicarnos con el cliente

# Confirmamos la petición del cliente
socketCliente.send("Petición recibida.".encode("utf-8"))

# Abrimos el archivo PDF en binario
archivo = open(nombreArchivo.decode("utf-8"), "rb")

# Enviamos el archivo PDF al cliente en binario
socketCliente.send(archivo.read())

# Cerramos el archivo
archivo.close()

# Cerramos el socket del Cliente y del Servidor
socketCliente.close()
socketServidor.close()
