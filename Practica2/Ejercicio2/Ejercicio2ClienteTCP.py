import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para la conexión UDP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecemos conexión con el servidor
socketCliente.connect((HOST, PORT))

# Enviamos al servidor el nombre del archivo PDF que queremos obtener
socketCliente.send("archivo.pdf".encode("utf-8"))

# Recibimos el mensaje de confirmación de petición
print(socketCliente.recv(1024).decode("utf-8"))

# Recibimos el archivo PDF del servidor
archivo = socketCliente.recv(1024)

# Creamos el archivo PDF
archivoPDF = open("archivoRecibido.pdf", "wb")

# Escribimos el archivo PDF
archivoPDF.write(archivo)

# Cerramos el archivo
archivoPDF.close()

# Cerramos el socket
socketCliente.close()
