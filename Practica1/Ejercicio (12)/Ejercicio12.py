import os


def copiar(origen, destino):
    if origen is None or destino is None:
        raise TypeError("Los parámetros deben ser no nulos")
    if type(origen) is not str or type(destino) is not str:
        raise TypeError("Los parámetros deben ser cadenas de texto, con extensión de archivo incluida")
    if not os.path.isfile(origen):
        raise OSError("El archivo origen no existe")
    with open(origen, 'r') as ficheroOrigen:
        with open(destino, 'w') as ficheroDestino:
            ficheroDestino.write(ficheroOrigen.read())


if __name__ == 'main':
    origen = 'original.txt'
    destino = 'copia.txt'
    copiar(origen,destino)