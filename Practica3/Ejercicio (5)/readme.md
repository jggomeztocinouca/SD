# Ejercicio 5
## Desarrollar con Bottle un servicio web que gestione el registro de usuarios de un sistema genérico (llamado "registroUsuarios.py"). El servicio web debe mantener una base de datos en memoria (puede estar vacía al arrancar el servicio) donde almacenar toda la información de los usuarios.
## Cada usuario contendrá los siguientes atributos (el alumno debe decidir qué tipo de datos usar para cada uno):
### → Nombre de usuario
### → Contraseña (puede almacenarse sin cifrar)
### → Cuenta activada (valor booleano)
### → Correo electrónico
### → Nombre y apellidos
### → Se deben implementar los siguientes endpoints:
#### → Registro de usuario: se añade un nuevo usuario indicando los atributos anteriormente mencionados. El atributo de cuenta activada deberá establecerse como "falso". No se podrá registrar un usuario si su nombre de usuario o correo electrónico ya están registrados en la base de datos.
#### → Activación de cuenta: dado un nombre de usuario o correo electrónico (que debe estar previamente registrado), se modificará la entrada de ese usuario en la base de datos, estableciendo como "verdadero" el atributo de cuenta activada. Es decir, el usuario debe existir previamente y el atributo de cuenta activada debe contener el valor "falso".
#### → Búsqueda de usuarios: dada una cadena de texto, se devolverán todos los usuarios que contengan esa cadena en el nombre de usuario o en el correo electrónico.
## Por último, se debe desarrollar una aplicación de terminal que sirva como cliente y tenga opciones de usar cualquiera de los endpoints descritos anteriormente.
## Se valorará negativamente una incompleta gestión de errores.