import socket

HOST = 'localhost' # Esta misma máquina
PORT = 1025 # Tiene que ser mayor que 1024

# Creamos el socket para establecer una conexión UDP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envíamos un mensaje al servidor
# sendto(message, (host_ip, host_port))
socketCliente.sendto("Hola Servidor, soy el Cliente".encode("utf-8"),(HOST,PORT))

# Cerramos el socket
socketCliente.close()