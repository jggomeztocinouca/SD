def get_file_info(filename = None):
    if filename is None:
        raise TypeError("NULL_ELEMENT")
    if type(filename) is not str:
        raise TypeError("NOT_INTEGER")
    if not os.path.exists(filename):
        raise OSError("FILE_NOT_FOUND")

    file_size = os.path.getsize(filename)

    words = []

    with open(filename) as file:
        for line in file:
            for word in line.split():
                if word.endswith('s'):
                    words.append(word)

    return(file_size,words)

print("Caso 1: La ruta introducida no es una cadena")
print("Ruta: 123")
try:
    get_file_info(123)
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta en formato distinto de cadena. Error:", mensajeError)

print("\nCaso 2: Ruta vacia")
print("Ruta: ")
try:
    get_file_info()
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta no especificada. Error:", mensajeError)

print("\nCaso 3: Ruta no existente")
print("Ruta: 'mifixero.txt'")
try:
    get_file_info("mifixero.txt")
except OSError as mensajeError:
    print("Excepcion capturada: Ruta no valida. Error:", mensajeError)

print("\nCaso general")
print("Ruta: 'mifichero.txt'")
print("Resultado:", get_file_info("mifichero.txt"))
