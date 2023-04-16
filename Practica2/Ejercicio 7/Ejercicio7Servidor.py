import socket
import os

def ls():
    return "\n **** Listado de ficheros del directorio actual **** \n" + "\n".join(os.listdir())


HOST = 'localhost' # Dirección IP del servidor
PORT = 1025 # Puerto del servidor

# Creamos el socket para establecer una conexión TCP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket con la dirección IP y el puerto
socketServidor.bind((HOST, PORT))

print("Server running!")

# Ponemos el socket a la escucha de peticiones de, cómo máximo, 1 cliente
socketServidor.listen(1)

# Aceptamos la conexión con el cliente
socketCliente, direccionCliente = socketServidor.accept()

print('Conexión establecida con el cliente: ' + str(direccionCliente))

# Enviamos el listado de opciones al cliente
socketCliente.send(((
    "1. Listar ficheros del directorio actual \n"
    "2. Recibir un archivo \n"
    "3. Salir"
                   ).encode('utf-8'))
)

opcion = "-1"
while opcion != "3":
    # Recibimos la opción elegida por el cliente
    opcion = socketCliente.recv(1024).decode('utf-8')
    if opcion == "1":
        # Enviamos la respuesta al cliente
        socketCliente.send(str(ls()).encode('utf-8'))
    elif opcion == "2":
        # Recibimos el nombre del archivo
        socketCliente.send("Nombre del archivo".encode('utf-8'))
        nombreArchivo = socketCliente.recv(1024).decode('utf-8')
        # Intentamos abrir el archivo
        try:
            archivo = open(nombreArchivo, 'rb')
            # Enviamos confirmación de existencia al cliente
            socketCliente.send("Archivo encontrado".encode('utf-8'))
            # Enviamos el archivo al cliente
            datos = archivo.read()
            socketCliente.sendall(datos)
            archivo.close()
        except FileNotFoundError:
            # Enviamos error de no existencia al cliente
            socketCliente.send("Archivo no encontrado".encode('utf-8'))

    elif opcion == "3":
        # Enviamos la respuesta al cliente
        socketCliente.send("Conexión cerrada".encode('utf-8'))
        # Cerramos la conexión con el cliente
        socketCliente.close()
        # Cerramos la conexión con el servidor
        socketServidor.close()
        print("Server closed!")