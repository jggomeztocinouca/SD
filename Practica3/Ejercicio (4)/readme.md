# Ejercicio 4
## Cree un servicio web de directorio similar al Directorio de la Universidad de Cádiz.

## El servicio deberá contar con un listado (evidentemente ficticio) del personal de la UCA, y cada miembro contará con los siguientes atributos:

### → DNI
### → Nombre completo
### → Correo electrónico
### → Departamento
### → Categoría (a elegir entre PAS/PDI/becario)
### → Lista de asignaturas (solo si es PDI)

## El servicio web deberá contar, al menos, con los siguientes endpoints:

### a) Dar de alta un miembro nuevo.

### b) Modificar los datos de un miembro.

### c) Consultar la lista de todos los miembros de la Universidad.

### d) Hacer una búsqueda por DNI.

### e) Obtener una lista de miembros según categoría.

## Queda a juicio del estudiante identificar qué tipo de operaciones HTTP debe implementar cada endpoint (PUT, POST o GET).

## Para los endpoints b), d) y e), es obligatorio el uso de parámetros en el path de la URL.

## Aunque hemos visto que REST permite transmitir los datos en cualquier formato, se recomienda utilizar JSON, tal y como se ha visto en el seminario.

## Se valorará positivamente el manejo adecuado de los errores (parámetros incorrectos, endpoint no encontrado, operaciones no permitidas) en el servicio y su notificación al cliente.

## Adicionalmente, implemente la siguiente funcionalidad:

### → Crear un endpoint para eliminar un miembro mediante una operación HTTP DELETE.

### → Utilizar alguna forma de persistencia de datos, almacenando la información de los miembros en un fichero o en una base de datos.

### → Habilitar una búsqueda parcial por nombre.

### → Habilitar una búsqueda paramétrica en la que se pueda elegir por qué criterio buscar.

### → Implementar una búsqueda inversa por asignaturas, listando los miembros PDI que pertenezcan a una asignatura.

### → Verificar que los datos introducidos al añadir un nuevo miembro son correctos, como por ejemplo la letra del DNI.

### → Otros endpoints adicionales que el estudiante considere oportunos.

## Por último, se debe crear un cliente que permita a un usuario interactuar con la API desarrollada.

## Este cliente le mostrará un menú al usuario con las posibles operaciones que se podrán realizar (de acuerdo a las implementadas en el servicio), solicitará los parámetros necesarios y realizará la llamada al servicio. Posteriormente, mostrará la información al usuario.

## Este cliente le mostrará un menú al usuario con las posibles operaciones que se podrán realizar (de acuerdo a las implementadas en el servicio), solicitará los parámetros necesarios y realizará la llamada al servicio. Posteriormente, mostrará la información al usuario.