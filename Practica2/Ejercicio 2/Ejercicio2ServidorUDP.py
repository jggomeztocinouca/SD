import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para la conexión UDP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asociamos el socket a la dirección y puerto
socketServidor.bind((HOST, PORT))

print("Server running!")

# Recibimos el nombre del archivo PDF que queremos obtener
nombreArchivo, direccionCliente = socketServidor.recvfrom(1024) # Usamos rcvfrom porque no sabemos de qué cliente nos van a llegar los datos

print("Petición entrante de " + str(direccionCliente) + " para el archivo '" + nombreArchivo.decode("utf-8") + "'")

aceptada = True

# Comprobamos si el archivo que nos quiere enviar el cliente ya existe en el directorio
try: # Intentamos abrir el archivo, si no existe, lanzará una excepción
    # Si existe, preguntamos al usuario si quiere sobreescribirlo
    archivo = open(nombreArchivo.decode("utf-8"), "rb")
    archivo.close()
    print("El archivo ya existe. ¿Desea sobreescribirlo? (S/N)")
    respuesta = input()
    if respuesta == "S" or respuesta == "s":
        socketServidor.sendto("Petición confirmada.".encode("utf-8"), direccionCliente)
    else:
        socketServidor.sendto("Petición rechazada.".encode("utf-8"), direccionCliente)
        aceptada = False
except: # Si el archivo no existe, se envía un mensaje de confirmación de petición
    socketServidor.sendto("Petición confirmada.".encode("utf-8"), direccionCliente)

# Abrimos el archivo PDF en binario y escritura
if aceptada:
    archivo = open(nombreArchivo.decode("utf-8"), "wb")
    archivo.write(socketServidor.recv(1024))
    socketServidor.sendto("Archivo recibido.".encode("utf-8"), direccionCliente)
    archivo.close()

# Cerramos el socket
socketServidor.close()
