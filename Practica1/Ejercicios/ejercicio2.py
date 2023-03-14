import os # Se importa el módulo necesario para acceder a la variable de entorno.

path = os.environ.get('PATH') # path, gracias al tipado dinámico, es un String que almacenará el contenido de la variable de entorno "PATH"

print("Variable de entorno: ")

print(path)
