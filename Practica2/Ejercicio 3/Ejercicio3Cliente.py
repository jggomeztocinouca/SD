import socket

HOST = 'localhost'
PORT = 1025

# Pedimos al usuario que introduzca el nombre del archivo y comprobamos que existe
existe = False
while(not existe):
    print("Introduzca el archivo que desea enviar (junto a la extensión de fichero)")
    nombreArchivo = input()
    try:
        archivo = open(nombreArchivo,"rb")
        archivo.close()
        existe = True
    except IOError:
        print("El archivo indicado no existe.")

# Creamos el socket para establecer una conexión TCP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el socket al servidor
socketCliente.connect((HOST,PORT))

# Enviamos el fichero
archivo = open(nombreArchivo,"rb")
socketCliente.sendall(archivo.read())

# Recibimos confirmación de que el archivo fue recibido correctamente
if socketCliente.recv(1024).decode("utf-8") == "Archivo recibido.":
    print("Archivo enviado.")
else:
    print("Error en el envío del archivo.")

archivo.close()

# Recibimos el archivo invertido y lo guardamos en texto plano
archivoInvertido = open("inverted" + nombreArchivo, "wb")
size = int(socketCliente.recv(1024).decode("utf-8"))
socketCliente.send("Tamaño recibido.".encode("utf-8"))
contenido = socketCliente.recv(size)
archivoInvertido.write(contenido)
print("Recibido archivo invertido: " + contenido.decode("utf-8"))
print("Tamaño: " + str(size) + " bytes")
archivoInvertido.close()
