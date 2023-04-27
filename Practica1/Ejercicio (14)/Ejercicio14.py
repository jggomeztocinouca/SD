import os

totalSize = 0
size = 0


# Recorre el directorio especificado en os.walk, en este caso el directorio de trabajo actual (.)
for rutaDirectorio, nombreDirectorios, nombresArchivo in os.walk('.'):
    for archivo in nombresArchivo:
        size = os.path.getsize(rutaDirectorio + '/' + archivo)
        totalSize += size
        print(f'{archivo}: {size} bytes.')

print(f'El tamaño total de los ficheros es de {totalSize} bytes')
