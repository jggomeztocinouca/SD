# Ejercicio 2
## Cree un programa cliente y un programa servidor en Python. 

### El programa cliente enviará un fichero (.pdf) al servidor, de acuerdo al siguiente flujo de interacción:

#### - El programa cliente establecerá una conexión con el servidor y solicitará enviarle un fichero al servidor, especificando el nombre del fichero.


#### - El servidor, recibida la petición del cliente, deberá responder afirmativamente. Sin embargo, si ya existe un fichero en el servidor con el mismo nombre del fichero que indica el cliente, el servidor, debe consultar al cliente si desea sobrescribir el fichero existente. En caso afirmativo, el servidor sobrescribiría el fichero. En caso negativo, se cancela la transferencia y se cierra la conexión.


#### - El cliente, una vez recibida la respuesta afirmativa, debe enviar el fichero al servidor, quien debe recibirlo y crear el fichero en su directorio de trabajo.


#### - El servidor debe notificar al cliente la recepción del fichero.


#### - El cliente, una vez recibida la notificación por parte del servidor, debe eliminar dicho fichero de su directorio de trabajo y cerrar la conexión con el servidor.

#### Implemente dos versiones distintas: una con TCP y otra con UDP.

#### La comunicación entre los procesos cliente/servidor debe realizarse utilizando únicamente sockets, no está permitido el uso de librerías de comunicación avanzadas.

#### Se deben utilizar ficheros binarios, en lugar de ficheros de texto, para poder enviar ficheros (.pdf) a través del socket correctamente