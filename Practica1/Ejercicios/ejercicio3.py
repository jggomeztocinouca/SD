import shutil
# shutil es un módulo en la biblioteca estándar de Python que proporciona varias funciones para trabajar con archivos y directorios.
# Está diseñado para simplificar las tareas de manipulación de archivos y directorios en Python.

import filecmp
# filecmp es un módulo en la biblioteca estándar de Python que proporciona funciones para comparar archivos y directorios.
# Está diseñado para simplificar la tarea de comparar el contenido de archivos y directorios en Python.

# Definimos el nombre del archivo original y el nombre de la copia
archivo_original = 'archivo_original.txt'
archivo_copia = 'archivo_copia.txt'

# Creamos la copia del archivo original
shutil.copy(archivo_original, archivo_copia) # Copia un archivo de origen a un archivo de destino. Si el archivo de destino ya existe, lo sobrescribe.

# Comprobamos si los archivos son iguales
if filecmp.cmp(archivo_original, archivo_copia): # Compara dos archivos y devuelve True si son idénticos en contenido y tamaño.
    print('Los archivos son iguales')
else:
    print('Los archivos son distintos')
