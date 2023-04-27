import os


def get_file_info(filename):
    if type(filename) is not str:
        raise TypeError("El parámetro debe ser una cadena de texto")
    if filename is None:
        raise TypeError("El parámetro debe ser no nulo")

    if not os.path.isfile(filename):
        raise OSError("El fichero no existe")

    size = os.path.getsize(filename)
    listaPalabras = []
    with open(filename, 'r') as fichero:
        for linea in fichero:
            for palabra in linea.split():
                if palabra[-1:] == 's':  # Si la última letra (-1 indica la última posición)
                    listaPalabras.append(palabra)

    return size, listaPalabras


if __name__ == 'main':
    print(get_file_info('mifichero.txt'))
