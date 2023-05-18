# Ejercicio 7
## Desarrollar con Bottle un servicio web para la gestión de un sistema de reserva de pistas de paddle (implementado en un fichero llamado "reservaPistas.py"). Las entradas y salidas de la API deberán hacerse en formato JSON. El servicio web debe mantener una base de datos en memoria (puede estar vacía al arrancar el servicio) donde almacenar toda la información de la reserva de pistas.
## Cada reserva de pista deberá contar con la siguiente información:
### → Identificador de reserva (generado por el sistema).
### → Número de pista reservada.
### → Hora de inicio (de 7 a 22, no hace falta guardar los minutos).
### → Hora de fin (de 8 a 23, no hace falta guardar los minutos).
### → Nombre del jugador que ha hecho la reserva.

## Se deben implementar los siguientes endpoints:
### → /reservar: deberá permitir añadir una nueva reserva para una pista concreta. Si la reserva es correcta, el sistema generará un identificador aleatorio que devolverá al usuario. En caso contrario, se deberá cancelar el proceso e informar al usuario si la pista ya está reservada para esa franja horaria.
### → /cancelar: dado un identificador de reserva, se eliminará la reserva asociada al identificador, quedando la pista liberada para esa franja horaria. En caso de que no exista ninguna reserva para ese identificador, deberá informarse al usuario del error.
### → /mostrar: dado un número de pista, el sistema deberá mostrar en qué franjas horarias la pista está ocupada y por quién. El formato del JSON de retorno queda a juicio del alumno, pero deberá ser suficiente para que un cliente pueda parsearlo para mostrar un listado con un aspecto similar al siguiente:

## Estado de la pista número 5:
### → 9:00 a 13:00: reservada por Juan
### → 18:00 a 20:00: reservada por Alfonso

## Notas:
### → El sistema gestionará un número N de pistas configurable.
### → Las reservas se hacen por horas y pueden durar una o más horas.
### → Las pistas se pueden reservar a partir de las 7:00, siendo la última hora reservable de 22:00 a 23:00.
### → El identificador de reserva deberá ser aleatorio.