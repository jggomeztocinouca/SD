import socket

HOST = 'localhost' # Dirección IP del servidor
PORT = 1025 # Puerto del servidor

# Creamos el socket para establecer una conexión TCP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecemos la conexión con el servidor
socketCliente.connect((HOST, PORT))

print('Conexión establecida con el servidor: ' + HOST + ':' + str(PORT))

# Recibimos el listado de opciones del servidor
opciones = socketCliente.recv(1024).decode('utf-8')
numOpciones = opciones.count('\n') + 1

opcion = -1
while opcion != int(numOpciones):
    # Imprimimos el listado de opciones y pedimos al usuario que elija una
    print("\n \nListado de opciones:")
    print(opciones)
    opcion = int(input("Elige una opción: "))
    if opcion <= 0 or opcion > numOpciones:
        print("Opción incorrecta. Inténtalo de nuevo.")
    else:
        socketCliente.send(str(opcion).encode('utf-8'))
        # Recibimos la respuesta del servidor
        respuesta = socketCliente.recv(1024).decode('utf-8')
        if respuesta == "Conexión cerrada":
            print("Conexión con el servidor finalizada.")
            socketCliente.close()
        elif respuesta == "Nombre del archivo":
            nombreArchivo = input("Introduce el nombre del archivo: ")
            socketCliente.send(nombreArchivo.encode('utf-8'))
            respuesta = socketCliente.recv(1024).decode('utf-8')
            if respuesta == "Archivo encontrado":
                print("Archivo encontrado. Descargando...")
                with open("copia_" + nombreArchivo, 'wb') as archivo:
                    while True:
                        datos = socketCliente.recv(1024)
                        if not datos:
                            break
                        archivo.write(datos)
                print("Archivo " + nombreArchivo + " descargado.")

            else:
                print("Archivo no encontrado en el servidor.")
        else:
            print(respuesta)




