import os
import shutil

ruta = "/home/jggomeztocino/CarpetaCopia"
for root, dirs, files in os.walk(ruta, topdown=False):  # Recorremos todos los archivos y subdirectorios a partir del directorio actual
	for name in files:  # Recorremos los archivos del directorio actual y los subdirectorios
	    src_path = os.path.join(root, name)  # Obtenemos la ruta completa del archivo
	    dst_path = os.path.join(os.getcwd(), name)  # Obtenemos la ruta completa del destino
	    shutil.move(src_path, dst_path)  # Movemos el archivo al directorio actual
	    print(f"{src_path} movido a {dst_path}")  # Imprimimos el archivo movido y su destino

