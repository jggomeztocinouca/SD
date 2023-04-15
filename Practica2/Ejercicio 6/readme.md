# Ejercicio 6
## Crear un programa cliente y un programa servidor que se comunicarán mediante sockets UDP. 
## El cliente podrá enviarle los siguientes comandos al servidor, los cuales podrá introducir el usuario a través del teclado:
### - ls: el servidor devolverá una lista con todos los ficheros de su directorio actual al cliente.
### - rm <nombre_fichero>: se borrará el fichero indicado en el directorio del servidor.
### - write <nombre_fichero> "mensaje": el servidor creará un fichero llamado <nombre_fichero> y escribirá el texto <mensaje> dentro de él.
### - exit: se cerrará la conexión y ambos programas finalizarán.
### - cd <nombre_directorio>: el cliente cambia el directorio de trabajo en el servidor. Si el directorio especificado no existe, el servidor debe devolver un error al cliente.
### - mv <origen> <destino>: el cliente mueve un fichero desde el directorio origen al directorio destino. Los directorios deben ser distintos. El servidor responderá al cliente indicándole si la operación se ha realizado correctamente, en caso contrario, el servidor debe devolver un error.

### Después de cada comando, excepto para ls, el servidor responderá al cliente indicándole si la operación se ha realizado correctamente.

