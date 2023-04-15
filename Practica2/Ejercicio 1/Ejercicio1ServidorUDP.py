import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para establecer la conexión UDP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazamos al socket la dirección y el puerto a usar
socketServidor.bind((HOST, PORT))

print("Server running!")

# Dejamos bloqueado al servidor (recvfrom es un método bloqueante) a la espera de recibir un mensaje
message, address = socketServidor.recvfrom(1024)

print("He recibido el siguiente mensaje desde la dirección " +
      str(address[0]) + ":" + str(address[1]) + ": " + message.decode("utf-8"))
socketServidor.close()