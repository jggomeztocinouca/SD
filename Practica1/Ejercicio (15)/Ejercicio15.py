import os
import shutil

# Recorremos el directorio actual y sus subdirectorios
for rutaDirectorio, nombresDirectorios, nombresArchivos in os.walk('.'):
    # Recorremos todos los archivos en el directorio actual
    for archivo in nombresArchivos:
        # Obtenemos la ruta completa del archivo
        rutaArchivo = rutaDirectorio + '/' + archivo
        if not os.path.isfile(archivo): # Si el archivo no se encuentra en el directorio actual
            # Movemos el archivo al directorio actual
            shutil.move(rutaArchivo, '.')