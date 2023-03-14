import os

try:
	# Imprimimos el directorio de trabajo actual
	print(f"Directorio de trabajo actual: {os.getcwd()}")

	# Imprimimos la lista de ficheros existentes en el directorio actual
	print("Ficheros existentes en el directorio actual:")
	for file in os.listdir("."):
	    if os.path.isfile(file):  # Nos aseguramos de que sea un archivo y no un directorio
		print(f"- {file}")

	# Pedimos al usuario el nombre del fichero a renombrar
	old_name = input("Introduce el nombre del fichero que quieres renombrar: ")

	# Pedimos al usuario el nuevo nombre del fichero
	new_name = input("Introduce el nuevo nombre del fichero: ")

	# Renombramos el fichero
	os.rename(old_name, new_name)
	print(f"El fichero {old_name} ha sido renombrado como {new_name}.")

except FileNotFoundError:
	print("El fichero que quieres renombrar no existe en el directorio actual.")
	
except FileExistsError:
	print("Ya existe un fichero con ese nombre en el directorio actual. Por favor, elige otro nombre.")
	
except OSError as e:
	print(f"Error al renombrar el fichero: {e}")

