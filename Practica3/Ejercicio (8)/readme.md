# Ejercicio 8 
## Desarrollo de un servicio web para la gestión de llegadas y salidas de aviones en un aeropuerto con Bottle

## Desarrollar con Bottle un servicio web en un fichero (llamado aeropuerto.py) para la gestión de llegadas (aterrizajes) y salidas (despegues) de aviones de un aeropuerto con dos pistas numeradas 10 y 30. El servicio web debe mantener una base de datos en memoria (puede estar vacía al arrancar el servicio) donde almacenar toda la información de los aviones que han pasado por el aeropuerto.

## Cada avión contendrá los siguientes atributos (el alumno debe decidir qué tipo de datos usar para cada uno):
### a. Matrícula (asignada manualmente).
### b. Fecha y hora de llegada.
### c. Número de pista de llegada.
### d. Fecha y hora de salida.
### e. Número de pista de salida.

## Se deben implementar los siguientes endpoints:
### - Registro de aterrizaje: se añade un nuevo avión al aeropuerto indicando la hora de aterrizaje y dejando vacíos (None) los atributos d) y e). El número de pista de llegada, asignada automáticamente, deberá ser aquella que aparezca con menor frecuencia en los aviones de la base de datos que siguen en tierra (aquellos con b) y c) rellenos, y None en d) y e)). El alumno puede elegir cualquier criterio de asignación de pista cuando no haya aviones en la base de datos.
### - Registro de despegue: indicando la matrícula del avión (que previamente debe estar en tierra) y una hora de salida, el número de pista de salida se asigna automáticamente siguiendo el mismo criterio que en el endpoint 1.
### - Listado de todos los aviones del aeropuerto y el valor de sus atributos.

