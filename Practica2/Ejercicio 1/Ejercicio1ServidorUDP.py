import socket

HOST = 'localhost'
PORT = 1025

# Creamos el socket para establecer la conexión UDP
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazamos al socket la dirección y el puerto a usar
s_udp.bind((HOST, PORT))

print("Server running!")

# Dejamos a bloqueado al servidor (recvfrom es un método bloqueante) a la espera de recibir un mensaje
message, address = s_udp.recvfrom(1024)

print("He recibido el siguiente mensaje desde la dirección " + str(address[0]) + ":" + str(address[1]) + ": " + message.decode("utf-8"))
s_udp.close()