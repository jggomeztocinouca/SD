# Ejercicio 5
## Crear un programa cliente y un programa servidor en Python. El programa servidor enviará una imagen de extensión .jpg al cliente, de acuerdo al siguiente flujo de interacción:
### - El programa cliente enviará al servidor el nombre de un fichero con extensión .jpg.
### - El servidor, recibida la petición del cliente, debe comprobar que el fichero existe. Si no es así, debe devolver un mensaje de error al cliente y finalizar.
### - Si el fichero existe, debe enviar el fichero al cliente, quien debe recibirlo y crear el fichero en su directorio de trabajo.

## Notas:
### Debe utilizarse TCP como protocolo de transporte.
### Tenga en cuenta que para poder enviar imágenes a través del socket correctamente, deben operarse como ficheros binarios, en vez de como ficheros de texto.
