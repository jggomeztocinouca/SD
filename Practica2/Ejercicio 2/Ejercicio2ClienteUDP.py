import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para la conexión UDP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviamos al servidor el nombre del archivo PDF que queremos enviar
socketCliente.sendto("archivo.pdf".encode("utf-8"), (HOST, PORT))
print("Petición enviada.")

# Recibimos el mensaje de confirmación/rechazo de petición
estado = socketCliente.recv(1024).decode("utf-8")
print(estado)
if estado == "Petición confirmada.":

    # Abrimos el archivo PDF en binario
    archivo = open("archivo.pdf", "rb")

    # Enviamos el archivo PDF al servidor en binario
    socketCliente.sendto(archivo.read(), (HOST, PORT))

    # Cerramos el archivo
    archivo.close()

    # Recibimos el mensaje de confirmación de recepción
    if socketCliente.recv(1024).decode("utf-8") == "Archivo recibido.":
        print("Archivo enviado correctamente.")
        # Eliminamos el archivo PDF
        import os
        os.remove("archivo.pdf")

# Cerramos el socket
socketCliente.close()
