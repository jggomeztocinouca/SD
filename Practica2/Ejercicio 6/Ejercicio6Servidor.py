import os
def ls():
    return os.listdir()

def rm(nombre):
    if os.path.isfile(nombre):
        os.remove(nombre)
    elif os.path.isdir(nombre):
        os.rmdir(nombre)
    else:
        return "No existe el fichero o directorio"

def write(nombre, mensaje):
    file = open(nombre, "w")
    file.write(mensaje)
    file.close()
    return "Fichero creado correctamente"

def cd(nombre):
    if os.path.isdir(nombre):
        os.chdir(nombre)
        return "Directorio cambiado correctamente"
    else:
        return "No existe el directorio"

# Mover fichero/directorio
def mv(dir_origen, dir_destino):
    if os.path.isfile(dir_origen):
        os.rename(dir_origen, dir_destino)
        return "Fichero movido correctamente"
    elif os.path.isdir(dir_origen):
        os.rename(dir_origen, dir_destino)
        return "Directorio movido correctamente"
    else:
        return "No existe el fichero o directorio"


import socket

HOST = 'localhost'
PORT = 1026

# Creamos el socket para establecer una conexión UDP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket a la dirección y puerto
socketServidor.bind((HOST, PORT))

print("Server running!")

# Ponemos el servidor a la escucha de peticiones de, como máximo, 1 cliente
socketServidor.listen(1)

# Aceptamos la conexión del cliente
socketCliente, direccionCliente = socketServidor.accept()
print("Conexión establecida con el cliente " + (str(direccionCliente)))

# Enviamos al cliente el mensaje de control de sesión
socketCliente.send("Sesión iniciada.".encode('utf-8'))

# Enviamos al cliente el listado de Opciones
socketCliente.send(("¡Bienvenido al servidor! \n"
                    "1. ls: Listar ficheros y directorios del servidor \n"
                    "2. rm <nombre>: Eliminar fichero/directorio \n"
                    "3. write <nombre> 'mensaje': Crear fichero y escribe el mensaje dentro de este \n"
                    "4. cd <nombre>: Cambiar directorio de trabajo \n"
                    "5. mv <dir_origen> <dir_destino>: Mover fichero/directorio \n"
                    "6. exit: Salir del servidor \n").encode('utf-8'))

# Recibimos la opción del cliente y comprobamos si es válida
option = -1
while option != 6:
    option = socketCliente.recv(1024).decode('utf-8')
    if option == "1":
        socketCliente.send("Opción valida".encode('utf-8'))
        socketCliente.send("Parámetros no necesarios".encode('utf-8'))
        socketCliente.send(ls().encode('utf-8'))
        socketCliente.send("Sesión continuada.".encode('utf-8'))
    elif option == "2":
        socketCliente.send("Opción valida".encode('utf-8'))
        socketCliente.send("Parámetros necesarios".encode('utf-8'))
        socketCliente.send("Introduce el nombre del fichero/directorio a eliminar: ".encode('utf-8'))
        nombre = socketCliente.recv(1024).decode('utf-8')
        socketCliente.send("Parámetros no necesarios".encode('utf-8'))
        socketCliente.send(rm(nombre))
        socketCliente.send("Sesión continuada.".encode('utf-8'))
    elif option == "3":
        socketCliente.send("Opción valida".encode('utf-8'))
        socketCliente.send("Parámetros necesarios".encode('utf-8'))
        socketCliente.send("Introduce el nombre del fichero a crear: ".encode('utf-8'))
        nombreArchivo = socketCliente.recv(1024).decode('utf-8')
        socketCliente.send("Parámetros necesarios".encode('utf-8'))
        socketCliente.send("Introduce el mensaje a escribir en el fichero: ".encode('utf-8'))
        mensaje = socketCliente.recv(1024).decode('utf-8')
        socketCliente.send("Parámetros no necesarios".encode('utf-8'))
        socketCliente.send(write(nombreArchivo, mensaje).encode('utf-8'))
        socketCliente.send("Sesión continuada.".encode('utf-8'))
    elif option == "4":
        socketCliente.send("Opción valida".encode('utf-8'))
        socketCliente.send("Parámetros necesarios".encode('utf-8'))
        socketCliente.send("Introduce el nombre del directorio a cambiar: ".encode('utf-8'))
        nombre = socketCliente.recv(1024).decode('utf-8')
        socketCliente.send("Parámetros no necesarios".encode('utf-8'))
        socketCliente.send(cd(nombre))
        socketCliente.send("Sesión continuada.".encode('utf-8'))
    elif option == "5":
        socketCliente.send("Opción valida".encode('utf-8'))
        socketCliente.send("Parámetros necesarios".encode('utf-8'))
        socketCliente.send("Introduce el directorio origen: ".encode('utf-8'))
        dir_origen = socketCliente.recv(1024).decode('utf-8')
        socketCliente.send("Parámetros necesarios".encode('utf-8'))
        socketCliente.send("Introduce el directorio destino: ".encode('utf-8'))
        dir_destino = socketCliente.recv(1024).decode('utf-8')
        socketCliente.send("Parámetros no necesarios".encode('utf-8'))
        socketCliente.send(mv(dir_origen, dir_destino))
        socketCliente.send("Sesión continuada.".encode('utf-8'))
    elif option == "6":
        socketCliente.send("Opción valida".encode('utf-8'))
        socketCliente.send("Sesión finalizada".encode('utf-8'))
    else:
        socketCliente.send("Opción no valida".encode('utf-8'))

# Cerramos la conexión
socketCliente.close()
socketServidor.close()
print("Conexión con cliente cerrada.")
print("Server closed!")