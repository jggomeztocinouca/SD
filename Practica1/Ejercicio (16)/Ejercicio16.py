import os


def listarArchivos():
    # Imprimimos el directorio actual
    print(f'Ruta del directorio actual: {os.getcwd()}')

    # Imprimimos el listado de los archivos contenidos en el directorio actual
    print("Listado de archivos del directorio:")
    for rutaDirectorio, nombresDirectorios, nombresArchivos in os.walk('.'):
        for archivo in nombresArchivos:
            print(archivo)


listarArchivos()

opcion = input("Desea modificar el nombre de algun fichero? (S/N) ")
if opcion == 'S' or opcion == 's':
    archivoRenombrar = input("Introduzca el nombre del fichero a renombrar: ")
    if type(archivoRenombrar) is not str:
        print("Error. Nombre de archivo introducido no valido.")
    elif archivoRenombrar is None:
        print("Error. El nombre del archivo no puede ser nulo")
    elif not os.path.isfile(archivoRenombrar):
        print("Error. El archivo introducido no existe")
    else:
        os.rename(archivoRenombrar, input("Introduzca el nuevo nombre: "))
        listarArchivos()
