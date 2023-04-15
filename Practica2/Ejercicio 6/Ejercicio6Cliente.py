import socket

HOST = 'localhost'
PORT = 1026

# Creamos el socket para establecer una conexión UDP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el socket con el servidor
socketCliente.connect((HOST, PORT))
print("Conexión establecida con el servidor (" + HOST + ":" + str(PORT) + ")")

# Ciclo de vida
while socketCliente.recv(1024).decode("utf-8") != "Sesión finalizada":
    # Recibimos el listado de opciones
    print(socketCliente.recv(1024).decode('utf-8'))

    # Enviamos la opción al servidor
    option = input("Introduce una opción: ")
    socketCliente.send(option.encode('utf-8'))

    # Recibimos la respuesta del servidor
    while socketCliente.recv(1024).decode('utf-8') == "Opcion no valida":
        print("Opción no válida")
        option = input("Introduce una opción: ")
        socketCliente.send(option.encode('utf-8'))

    # Mandamos los parámetros necesarios
    while socketCliente.recv(1024).decode('utf-8') == "Parámetros necesarios":
        print(socketCliente.recv(1024).decode('utf-8'))
        socketCliente.send(input().encode('utf-8'))

    # Recibimos la respuesta del servidor
    print(socketCliente.recv(1024).decode('utf-8'))

# Cerramos la conexión
socketCliente.close()
print("Sesión finalizada")
