import socket

HOST = 'localhost'
PORT = 1025

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((HOST, PORT))

nombreImagen = input('Introduzca el nombre de la imagen a descargar: ')

socketCliente.send(nombreImagen.encode('utf-8'))

existe = False

if socketCliente.recv(1024).decode('utf-8') == 'existe':
    existe = True

if existe:
    with open('descargada_' + nombreImagen, 'wb') as imagen:
        datos = socketCliente.recv(4096)
        while datos:
            imagen.write(datos)
            datos = socketCliente.recv(4096)
    print('Imagen recibida')

socketCliente.close()
