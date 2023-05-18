# Ejercicio 3
## Desarrolle un servicio web de gestión de habitaciones de un hotel. El servicio debe poseer una lista de habitaciones y cada habitación poseerá, mínimo, los siguientes atributos:

### → Identificador.
### → Número de plazas.
### → Lista de equipamiento (por ejemplo: armario, aire acondicionado, caja fuerte, escritorio, etc.).
### → Ocupada (sí/no).
## Se deben implementar los siguientes endpoints:

### a) Dar de alta una nueva habitación.

### b) Modificar los datos de una habitación.

### c) Consultar la lista completa de habitaciones.

### d) Consultar una habitación mediante identificador.

### e) Consultar la lista de habitaciones ocupadas o desocupadas.

## Queda a juicio del estudiante identificar qué tipo de operaciones HTTP debe implementar cada endpoint (PUT, POST o GET).

## Para los endpoints b), d) y e), es obligatorio el uso de parámetros en el path de la URL.

## Aunque hemos visto que REST permite transmitir los datos en cualquier formato, se recomienda utilizar JSON, tal y como se ha visto en el seminario.

## Se valorará positivamente el manejo adecuado de los errores (parámetros incorrectos, endpoint no encontrado, operaciones no permitidas) en el servicio y su notificación al cliente.

## Como mejoras puede practicar lo siguiente:

### → Crear un endpoint para eliminar una habitación mediante una operación HTTP DELETE.

### → Hacer que la información que maneja el servicio sea persistente, almacenando la información de las habitaciones en un fichero.

### → Crear una clase "Room" para facilitar el manejo de la información por parte del servicio.

### → Crear los endpoints adicionales que el estudiante considere oportuno.

## Por último, se debe crear un cliente que permita a un usuario interactuar con la API desarrollada.

## Este cliente le mostrará un menú al usuario con las posibles operaciones que se podrán realizar (de acuerdo a las implementadas en el servicio), solicitará los parámetros necesarios y realizará la llamada al servicio. Posteriormente, mostrará la información al usuario.