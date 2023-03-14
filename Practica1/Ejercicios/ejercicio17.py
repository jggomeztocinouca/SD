import os

try:
	# Creamos un archivo nuevo llamado "union.txt"
	with open("union.txt", "w") as f_union:
	    # Recorremos todos los ficheros del directorio actual
	    for file in os.listdir("."):
		# Nos aseguramos de que sea un archivo de texto y no un directorio
		if os.path.isfile(file) and file.endswith(".txt"):
		    # Abrimos cada fichero de texto y lo leemos
		    with open(file, "r") as f:
		        content = f.read()
		    # Escribimos el contenido en el archivo "union.txt"
		    f_union.write(content)

	print("Los ficheros de texto han sido combinados en el archivo 'union.txt'.")

except Exception as e:
	print(f"Error al combinar los ficheros de texto: {e}")


