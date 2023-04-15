import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para establecer una conexión TCP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket a la dirección y puerto del host
socketServidor.bind((HOST, PORT))

print("Server running!")

# Ponemos al servidor a la escucha de peticiones de, como máximo, 1 cliente
socketServidor.listen(1)

# Aceptamos la conexión y creamos un nuevo socket para el cliente aceptado
socketCliente, direccionCliente = socketServidor.accept()

# Impresión de información del cliente
print("Petición de conexión recibida de: " + str(direccionCliente))

# Recibimos el fichero a invertir
archivo = socketCliente.recv(1024)

# Enviamos confirmación de que el archivo fue recibido correctamente
print("Archivo recibido: " + archivo.decode("utf-8"))
socketCliente.sendall("Archivo recibido.".encode("utf-8"))

# Invertimos el contenido del fichero
archivo = archivo[::-1] # Recorrido inverso

# Calculamos el tamaño del fichero
size = str(len(archivo))

# Enviamos el tamaño del fichero y luego el archivo invertido
socketCliente.sendall(size.encode("utf-8"))
if socketCliente.recv(1024).decode("utf-8") == "Tamaño recibido.":
    socketCliente.sendall(archivo)
    print("Enviado archivo invertido: " + archivo.decode("utf-8"))
    print("Tamaño: " + size + " bytes")
else:
    print("Error en el envío del archivo.")

# Cerramos el socket del cliente
socketCliente.close()

# Cerramos el socket del servidor
socketServidor.close()

print("Server closed!")
