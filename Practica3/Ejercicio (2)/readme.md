# Ejercicio 2
## Escriba el código correspondiente a un endpoint de tipo POST con el framework Bottle en Python.

## El nombre del endpoint será /inserta. Como entrada tomará un JSON, en el que se encontrará un número entero cuya clave será elemento. El servidor buscará el número indicado en el JSON de entrada en un array denominado mis_elementos, si el elemento no existe en el array lo insertará en la última posición, en caso contrario, no modificará el array.
## Por último, devolverá al cliente, también en formato JSON, el array resultante con la clave mis_elementos. Si la clave elemento no se encuentra en el JSON de entrada, el servicio deberá devolver un error al cliente.
