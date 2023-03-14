import os

def copiar(archivo_original = None, archivo_copia = None):
    if archivo_original is None or archivo_copia is None:
        raise TypeError("NULL_ELEMENT")
    if type(archivo_original) is not str or type(archivo_copia) is not str:
        raise TypeError("NOT_INTEGER")
    if not os.path.exists(archivo_original) or not os.path.exists(archivo_copia):
        raise OSError("FILE_NOT_FOUND")

    with open(archivo_original,'rb') as original:
        with open(archivo_copia,'wb') as copia:
            contenido = original.read()
            copia.write(contenido)

print("Caso 1: La ruta introducida no es una cadena")
print("Ruta 1: 123, Ruta 2: 'archivo_copia.txt'")
try:
    copiar(123, "archivo_copia.txt")
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta en formato distinto de cadena. Error:", mensajeError)

print("\nCaso 2: Ruta vacia")
print("Ruta 1: , Ruta 2: ")
try:
    copiar()
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta no especificada. Error:", mensajeError)

print("\nCaso 3: Ruta no existente")
print("Ruta 1: 'arxivo_original.txt', Ruta 2: 'archivo_copia.txt'")
try:
    copiar('arxivo_original.txt', "archivo_copia.txt")
except OSError as mensajeError:
    print("Excepcion capturada: Ruta no valida. Error:", mensajeError)

print("\nCaso general")
print("Ruta 1: 'archivo_original.txt', Ruta 2: 'archivo_copia.txt'")
copiar("archivo_original.txt", "archivo_copia.txt")
if filecmp.cmp("archivo_original.txt", "archivo_copia.txt"): # Compara dos archivos y devuelve True si son idénticos en contenido y tamaño.
    print('Resultado: Los archivos son iguales')
else:
    print('Resultado: Los archivos son distintos')
