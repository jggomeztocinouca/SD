import os

print("Listado de directorios:")
# El fichero '/etc/passwd, que contiene información de los usuarios del sistema, incluyendo su directorio de inicio.
with open('/etc/passwd') as file:
	for line in file:
	    home_dir = line.split(':')[5]
	    print(home_dir)

