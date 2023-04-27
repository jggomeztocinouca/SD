# Ejercicio 9
## Implemente la función get_file_info(filename) para que devuelva una tupla con el tamaño en bytes del fichero, cuyo nombre se indica como parámetro filename,  en la primera posición, y una lista con las palabras acabadas con el carácter 's' que contenga el fichero, en segunda posición.
### Por ejemplo, la invocación get_file_info('mifichero.txt'), suponiendo que 'mifichero.txt' contiene el texto  “La casa está pintada en muchos colores'', devolverá la tupla (39, ['muchos', 'colores']).
## Se deberán generar las siguientes excepciones en caso de ser necesario:
### ■ TypeError si el parámetro filename no es una cadena o es nulo (None).
### ■ OSError si el fichero indicado no existe