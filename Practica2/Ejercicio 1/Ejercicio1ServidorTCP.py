import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket del servidor para establecer la conexión TCP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket a la dirección y puerto del host especificado
socketServidor.bind((HOST,PORT))

print("Server running!")

# Ponemos el socket a la escucha de, como máximo, 1 petición
socketServidor.listen(1) # Operación bloqueante

# Una vez entrada una petición, asignaremos al cliente un nuevo socket propio
# para comunicarnos con él
socketCliente, address = socketServidor.accept()

# Recibimos el mensaje del cliente
print("Conexión entrante: " + str(address) + ". Mensaje recibido: " + socketCliente.recv(1024).decode("utf-8"))

# Enviamos un mensaje al cliente
socketCliente.send("Hola cliente! Este es nuestro canal propio.".encode("utf-8"))

# Una vez realizadas las acciones, cerramos tantos sockets como hayamos abierto
socketCliente.close()
socketServidor.close()