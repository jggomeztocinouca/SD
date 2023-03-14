import os

total_size = 0  # Inicializamos la variable que acumulará el tamaño total de los archivos

for root, dirs, files in os.walk(".", topdown = False):  # Recorremos todos los archivos y subdirectorios a partir del directorio actual
	for name in files:  # Recorremos los archivos del directorio actual y los subdirectorios
	    path = os.path.join(root, name)  # Obtenemos la ruta completa del archivo
	    size = os.path.getsize(path)  # Obtenemos el tamaño del archivo en bytes
	    total_size += size  # Sumamos el tamaño del archivo a la variable total_size
	    print(f"{path}: {size} bytes")  # Imprimimos el nombre del archivo y su tamaño en bytes

print(f"Total size: {total_size} bytes")  # Imprimimos el tamaño total de todos los archivos

