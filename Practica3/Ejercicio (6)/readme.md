# Ejercicio 6
## Desarrollar con Bottle un servicio web que gestione un servicio de alquiler de vehículos. El servicio web debe mantener dos bases de datos en memoria (pueden estar vacías al arrancar el servidor) donde almacenar toda la información de los vehículos y los clientes activos (con vehículos alquilados).
## Cada vehículo contendrá los siguientes atributos (el alumno debe decidir qué tipo de datos usar para cada uno):
### → ID vehículo
### → Marca
### → Modelo
### → Estado de alquiler (alquilado o no alquilado)
### → Actual o último usuario que lo ha alquilado
## Cada usuario contendrá los siguientes atributos (el alumno debe decidir qué tipo de datos usar para cada uno):
### → ID usuario
### → Número de veces que ha alquilado un vehículo
## Se deben implementar los siguientes endpoints (el alumno debe decidir qué tipo de método usar en cada caso):
### → Registro de usuario: se añade un nuevo usuario asignándole automáticamente un ID único e inicializando el número de alquileres a 0.
### → Registro de vehículo: se añade un nuevo vehículo a la flota disponible para alquilar. Hay que asignarle automáticamente un ID único y pasarle la información de marca y modelo mediante un JSON. Se debe inicializar el estado del alquiler como no alquilado.
### → Alquiler de un vehículo libre: dado un ID de usuario, localizar un vehículo cualquiera libre y asignárselo al usuario. El alumno debe actualizar el campo estado de alquiler del vehículo y el campo número de veces que ha alquilado un vehículo del usuario.
### → Alquiler de un vehículo específico: dados los IDs de usuario y vehículo, asignar el vehículo al usuario. El alumno debe actualizar el campo estado de alquiler del vehículo y el campo número de veces que ha alquilado un vehículo del usuario.
### → El alumno debe gestionar los posibles errores que puedan ocurrir al usar estos endpoints (por ejemplo, que se quiera alquilar un vehículo, pero no queden vehículos libres).




