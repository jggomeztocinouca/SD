# Ejercicio 1
## Probar Sockets
### 1. Implemente un programa cliente/servidor que comunique dos procesos con los protocolos TCP y UDP
Véase los ficheros Ejercicio1Cliente.py y Ejercicio1Servidor.py

### 2. Explique las diferencias entre los protocolos TCP y UDP
Respuesta

### 3. ¿Qué ocurre si el cliente se inicia antes que el servidor en ambos casos (TCP y UDP)?
En el protocolo UDP, si iniciamos el cliente antes que el servidor, el mensaje simplemente se perderá.

En cambio, en el protocolo TCP, si iniciamos el cliente antes que el servidor, 
el cliente comprobará que no puede establecer conexión y cancelará el envío.