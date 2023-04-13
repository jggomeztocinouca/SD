import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket
socketServidor.bind((HOST, PORT))

print("Server running!")

# Ponemos el servidor a la escucha de peticiones de, como máximo, 1 cliente
socketServidor.listen(1)

# Aceptamos la conexión y creamos un nuevo socket para comunicarnos con el cliente
socketCliente, direccionCliente = socketServidor.accept()
print("Conexión entrante de " + str(direccionCliente))

# Enviamos el mensaje
socketCliente.send("¡Bienvenido! ¿Cuál es su nombre para que pueda dirigirme a usted?".encode("utf-8"))

# Recibimos el mensaje
nombre = socketCliente.recv(1024).decode("utf-8")

# Enviamos el mensaje
socketCliente.send(("¡Hola " + nombre + "! ¿En qué puedo ayudarte?").encode("utf-8"))

# Enviamos la misma respuesta hasta que el cliente introduzca "exit"
while socketCliente.recv(1024).decode("utf-8") != "exit":
    socketCliente.send("Debe ponerse en contacto con el servicio de atención de dudas cuya dirección es dudas@ejemplo.com".encode("utf-8"))

# Enviamos el mensaje de despedida
socketCliente.send("¡Hasta pronto!".encode("utf-8"))

# Cerramos el socket
socketCliente.close()
socketServidor.close()

print("Server closed!")