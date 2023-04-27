import os

# Creamos el archivo union.txt
with open('union.txt','w') as archivoUnion:
    for archivo in os.listdir('.'):
        if archivo.endswith('.txt') and os.path.isfile(archivo):
            with open(archivo, 'r') as archivoIndividual:
                archivoUnion.write(archivoIndividual.read() + '\n')