import math

print("-------------------------------------------------------------- EJERCICIO 2 --------------------------------------------------------------")

# Existe una variable de entorno que nos permite ejecutar comandos ubicados en /bin, sin necesidad de escribir la ruta completa,
# ni situarnos en el directorio en cuestión, muestra en pantalla el valor que contiene.
# ¿Qué módulo permite ver esto usando import nombreDelModulo al principio del script?

# RESPUESTA: Esta variable de entorno es "PATH", que puede ser accedida en Pyhton mediante el módulo "os"

import os # Se importa el módulo necesario para acceder a la variable de entorno.
path = os.environ.get('PATH') # path, gracias al tipado dinámico, es un String que almacenará el contenido de la variable de entorno "PATH"
print("Variable de entorno: ")
print(path)

print("\n-------------------------------------------------------------- EJERCICIO 3 --------------------------------------------------------------")
# Haga un script en Python que cree una copia de un fichero cualquiera.
# Puede implementar una función propia o utilizar una existente.
# A continuación, utilice la librería/módulo necesario para comprobar que los ficheros anteriores son iguales.

import shutil
# shutil es un módulo en la biblioteca estándar de Python que proporciona varias funciones para trabajar con archivos y directorios.
# Está diseñado para simplificar las tareas de manipulación de archivos y directorios en Python.

import filecmp
# filecmp es un módulo en la biblioteca estándar de Python que proporciona funciones para comparar archivos y directorios.
# Está diseñado para simplificar la tarea de comparar el contenido de archivos y directorios en Python.

# Definimos el nombre del archivo original y el nombre de la copia
archivo_original = 'archivo_original.txt'
archivo_copia = 'archivo_copia.txt'

# Creamos la copia del archivo original
shutil.copy(archivo_original, archivo_copia) # Copia un archivo de origen a un archivo de destino. Si el archivo de destino ya existe, lo sobrescribe.

# Comprobamos si los archivos son iguales
if filecmp.cmp(archivo_original, archivo_copia): # Compara dos archivos y devuelve True si son idénticos en contenido y tamaño.
    print('Los archivos son iguales')
else:
    print('Los archivos son distintos')

print("\n-------------------------------------------------------------- EJERCICIO 4 --------------------------------------------------------------")
# Implemente la función accum(x, y, z) para que devuelva la suma de # aquellos parámetros que incluyan un número par.
# Por ejemplo, la # invocación accum(5, 4, 2) deberá devolver como resultado 6.
# Se deberán generar las siguientes excepciones en caso de ser necesario:
# ■ TypeError si alguno de los tres argumentos x, y, o z no es un valor entero.

def accum(x,y,z):
    if not (type(x) is int and type(y) is int and type(z) is int):
        raise TypeError("NOT_INTEGER")

    resultado = 0

    if x%2 == 0:
        resultado += x

    if y % 2 == 0:
        resultado += y

    if z%2 == 0:
        resultado += z

    return resultado

print("Caso 1: Caracter no entero.")
print("Dato 1 = a, Dato 2 = 2, Dato 3 = 3.")
try:
    accum('a',2,3) # Devuelve excepción
except TypeError as mensajeError:
    print("Excepcion capturada, introducido caracter no entero. Codigo excepcion:", mensajeError)

print("\nCaso 2: Suma parcial de los parametros (hay algun numero no par).")
print("Dato 1 = 1, Dato 2 = 2, Dato 3 = 3.")
print(accum(1,2,3)) # Devuelve 2

print("\nCaso 3: Suma total de los parametros (todos los numeros son pares).")
print("Dato 1 = 2, Dato 2 = 4, Dato 3 = 6.")
print("Resultado:", accum(2,4,6)) # Devuelve 12

print("\n-------------------------------------------------------------- EJERCICIO 5 --------------------------------------------------------------")
# Implemente la función list_add(mylist, e) para que añada el elemento e # a la lista mylist y devuelva la lista resultante.
# Por ejemplo, la invocación de list_add([5, 2], 4) deberá devolver como resultado [5, 2, 4].
# Se deberán generar las siguientes excepciones en caso de ser necesario:
# ■ TypeError si el elemento e es nulo (None).

def list_add(mylist, e = None):
    if e is None:
        raise TypeError("NULL_ELEMENT")
    mylist.append(e)
    return mylist

print("Caso 1: Elemento Nulo introducido")
print("Dato 1: [5,2], Dato 2: ")
try:
    list_add([5,2])
except TypeError as mensajeError:
    print("Excepcion capturada: Elemento nulo introducido. Error:", mensajeError)

print("\nCaso general")
print("Dato 1: [5,2], Dato 2: 4")
print("Resultado:", list_add([5,2],4))

print("\n-------------------------------------------------------------- EJERCICIO 6 --------------------------------------------------------------")
# Implemente la función list_del(mylist, e) para que elimine la primera ocurrencia del elemento e de la lista mylist y devuelva la lista resultante.
# Por ejemplo, la invocación list_del([5, 2, 4], 2) deberá devolver como # resultado [5, 4].
# Se deberán generar las siguientes excepciones en caso de ser necesario:
# ■ TypeError si el elemento e es nulo (None) o la lista mylist está vacía

def list_del(mylist, e = None):
    if e is None:
        raise TypeError("NULL_ELEMENT")
    if not mylist:
        raise TypeError("EMPTY_LIST")
    try:
        mylist.remove(e)
    except ValueError:
        raise TypeError("NOT_FOUND")
    return mylist

print("Caso 1: Elemento Nulo introducido")
print("Dato 1: [5,2], Dato 2: ")
try:
    list_del([5,2])
except TypeError as mensajeError:
    print("Excepcion capturada: Elemento nulo introducido. Error:", mensajeError)

print("\nCaso 2: Lista vacia")
print("Dato 1: [], Dato 2: 2")
try:
    list_del([],2)
except TypeError as mensajeError:
    print("Excepcion capturada: Lista vacia. Error:", mensajeError)

print("\nCaso 3: Elemento no encontrado en la lista")
print("Dato 1: [5,2,4], Dato 2: 1")
try:
    list_del([5,2,4],1)
except TypeError as mensajeError:
    print("Excepcion capturada: Elemento no encontrado. Error:", mensajeError)

print("\nCaso general")
print("Dato 1: [5,2,4], Dato 2: 2")
print("Resultado:", list_del([5,2,4],4))

print("\n-------------------------------------------------------------- EJERCICIO 7 --------------------------------------------------------------")
# Implemente la función dict_add(mydict, t) para que añada la tupla (clave, valor) t pasada por parámetro al diccionario mydict.
# Por ejemplo, la invocación dict_add({1: 'manzana'}, {2, 'fresa'})} deberá devolver como resultado {1: 'manzana', 2: 'fresa'}.
# Se deberán generar las siguientes excepciones en caso de ser necesario:
# ■ TypeError si el elemento t es nulo (None) o no es una tupla de dos elementos.

def dict_add(mydict, t = None):
    if t is None:
        raise TypeError("NULL_ELEMENT")
    if len(t) != 2:
        raise TypeError("INCOMPLETE_PAIR")
    clave, valor = t
    mydict[clave] = valor
    return mydict

print("Caso 1: Elemento Nulo introducido")
print("Dato 1: {1: 'Hola'}, Dato 2: ")
try:
    dict_add({1: "Hola"})
except TypeError as mensajeError:
    print("Excepcion capturada: Elemento nulo introducido. Error:", mensajeError)

print("\nCaso 2: La tupla no es de dos elementos")
print("Dato 1: {1: 'Hola'}, Dato 2: (2)")
try:
    dict_add({1:"Hola"},(2,))
except TypeError as mensajeError:
    print("Excepcion capturada: Tupla erronea. Error:", mensajeError)

print("\nCaso general")
print("Dato 1: {1: 'Hola'}, Dato 2: (2:'Adios')")
print("Resultado:", dict_add({1:"Hola"},(2,"Adios")))

print("\n-------------------------------------------------------------- EJERCICIO 8 --------------------------------------------------------------")
# Implemente la función prime(a, b) para que devuelva una lista con los números primos en el intervalo cerrado [a, b].
# Por ejemplo, la invocación prime(2, 10) deberá devolver como resultado [2, 3, 5, 7].
# Se deberán generar las siguientes excepciones en caso de ser necesario:
# ■ TypeError si los parámetros a o b no son enteros o son nulos (None).

def prime(inicio = None, fin = None):
    if inicio is None or fin is None:
        raise TypeError("NULL_ELEMENT")
    if not(type(inicio) is int and type(fin) is int):
        raise TypeError("NOT_INTEGER")
    numPrimos = []
    for num in range(inicio,fin+1):
        if (num > 1):
            esPrimo = True
            for i in range(2,num):
                if (num % i) == 0:
                    esPrimo = False
                    break
            if esPrimo:
                numPrimos.append(num)
    return numPrimos

print("Caso 1: Elemento nulo introducido")
print("Dato 1: 2, Dato 2: ")
try:
    prime(1)
except TypeError as mensajeError:
    print("Excepcion capturada: Elemento nulo introducido. Error:", mensajeError)

print("\nCaso 2: Elemento no entero introducido")
print("Dato 1: 'a', Dato 2: 10")
try:
    prime("a",10)
except TypeError as mensajeError:
    print("Excepcion capturada: Elemento no entero introducido. Error:", mensajeError)

print("\nCaso general")
print("Dato 1: 2, Dato 2: 10")
print("Resultado:", prime(2,10))

print("\n-------------------------------------------------------------- EJERCICIO 9 --------------------------------------------------------------")
# Implemente la función get_file_info(filename) para que devuelva una tupla con el tamaño en bytes del fichero,
# cuyo nombre se indica como parámetro filename, en la primera posición,
# y una lista con las palabras acabadas con el carácter 's' que contenga el fichero, en segunda posición.
# Por ejemplo, la invocación get_file_info('mifichero.txt'),
# suponiendo que 'mifichero.txt' contiene el texto "La casa está pintada en muchos colores",
# devolverá la tupla (39, ['muchos', 'colores']).
# Se deberán generar las siguientes excepciones en caso de ser necesario:
# ■ TypeError si el parámetro filename no es una cadena o es nulo (None).
# ■ OSError si el fichero indicado no existe.

def get_file_info(filename = None):
    if filename is None:
        raise TypeError("NULL_ELEMENT")
    if type(filename) is not str:
        raise TypeError("NOT_INTEGER")
    if not os.path.exists(filename):
        raise OSError("FILE_NOT_FOUND")

    file_size = os.path.getsize(filename)

    words = []

    with open(filename) as file:
        for line in file:
            for word in line.split():
                if word.endswith('s'):
                    words.append(word)

    return(file_size,words)

print("Caso 1: La ruta introducida no es una cadena")
print("Ruta: 123")
try:
    get_file_info(123)
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta en formato distinto de cadena. Error:", mensajeError)

print("\nCaso 2: Ruta vacia")
print("Ruta: ")
try:
    get_file_info()
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta no especificada. Error:", mensajeError)

print("\nCaso 3: Ruta no existente")
print("Ruta: 'mifixero.txt'")
try:
    get_file_info("mifixero.txt")
except OSError as mensajeError:
    print("Excepcion capturada: Ruta no valida. Error:", mensajeError)

print("\nCaso general")
print("Ruta: 'mifichero.txt'")
print("Resultado:", get_file_info("mifichero.txt"))

print("\n-------------------------------------------------------------- EJERCICIO 10 --------------------------------------------------------------")
# Implemente una función en Python que realice la intersección de dos listas.
# Tenga en cuenta que no puede haber elementos repetidos.

def insersection(list1 = None, list2 = None):
    if not(list1 and list2):
        raise TypeError("EMPTY_LIST")

    list1 = list(set(list1)) # Creamos un set a partir de la lista para eliminar la duplicidad, y lo casteamos a lista de nuevo
    list2 = list(set(list2))  # Creamos un set a partir de la lista para eliminar la duplicidad, y lo casteamos a lista de nuevo

    finalList = []

    for item in list1:
        if item in list2:
            finalList.append(item)

    return finalList

print("Caso 1: Lista vacia")
try:
    insersection()
except TypeError as mensajeError:
    print("Excepcion capturada: Lista vacia. Error: ", mensajeError)

print("\nCaso general")
print("Dato 1: [1,2,3,4,4,5], Dato 2: [2,2,4,6,8,10]")
print("Resultado:", insersection([1,2,3,4,4,5],[2,2,4,6,8,10]))

print("\n-------------------------------------------------------------- EJERCICIO 11 --------------------------------------------------------------")
# Implemente una función en Python que realice la unión de dos listas.
# Tenga en cuenta que no puede haber elementos repetidos.

def union(list1 = None, list2 = None):
    if not(list1 and list2):
        raise TypeError("EMPTY_LIST")

    list1 = list(set(list1)) # Creamos un set a partir de la lista para eliminar la duplicidad, y lo casteamos a lista de nuevo
    list2 = list(set(list2))  # Creamos un set a partir de la lista para eliminar la duplicidad, y lo casteamos a lista de nuevo

    finalList = []

    for item in list1:
        finalList.append(item)

    for item in list2:
        if item not in list1:
            finalList.append(item)

    return finalList

print("Caso 1: Lista vacia")
try:
    union()
except TypeError as mensajeError:
    print("Excepcion capturada: Lista vacia. Error: ", mensajeError)

print("\nCaso general")
print("Dato 1: [1,2,3,4,4,5], Dato 2: [2,2,4,6,8,10]")
print("Resultado:", union([1,2,3,4,4,5],[2,2,4,6,8,10]))

print("\n-------------------------------------------------------------- EJERCICIO 12 --------------------------------------------------------------")
# Implemente una función copiar(origen,destino) que copie el contenido del fichero origen, en el fichero destino (usando open()).
def copiar(archivo_original = None, archivo_copia = None):
    if archivo_original is None or archivo_copia is None:
        raise TypeError("NULL_ELEMENT")
    if type(archivo_original) is not str or type(archivo_copia) is not str:
        raise TypeError("NOT_INTEGER")
    if not os.path.exists(archivo_original) or not os.path.exists(archivo_copia):
        raise OSError("FILE_NOT_FOUND")

    with open(archivo_original,'rb') as original:
        with open(archivo_copia,'wb') as copia:
            contenido = original.read()
            copia.write(contenido)

print("Caso 1: La ruta introducida no es una cadena")
print("Ruta 1: 123, Ruta 2: 'archivo_copia.txt'")
try:
    copiar(123, "archivo_copia.txt")
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta en formato distinto de cadena. Error:", mensajeError)

print("\nCaso 2: Ruta vacia")
print("Ruta 1: , Ruta 2: ")
try:
    copiar()
except TypeError as mensajeError:
    print("Excepcion capturada: Ruta no especificada. Error:", mensajeError)

print("\nCaso 3: Ruta no existente")
print("Ruta 1: 'arxivo_original.txt', Ruta 2: 'archivo_copia.txt'")
try:
    copiar('arxivo_original.txt', "archivo_copia.txt")
except OSError as mensajeError:
    print("Excepcion capturada: Ruta no valida. Error:", mensajeError)

print("\nCaso general")
print("Ruta 1: 'archivo_original.txt', Ruta 2: 'archivo_copia.txt'")
copiar("archivo_original.txt", "archivo_copia.txt")
if filecmp.cmp("archivo_original.txt", "archivo_copia.txt"): # Compara dos archivos y devuelve True si son idénticos en contenido y tamaño.
    print('Resultado: Los archivos son iguales')
else:
    print('Resultado: Los archivos son distintos')

print("\n-------------------------------------------------------------- EJERCICIO 13 --------------------------------------------------------------")
# Imprima por pantalla el listado de directorios de inicio de los usuarios que hay en el sistema (p. ej., /home/root , /home/osboxes, . . . ).
# Pista: hay un fichero con esta información.
# También existe una función muy interesante en Python llamada split, que convierte de string a lista.

def print_directory():
    # El fichero '/etc/passwd, que contiene información de los usuarios del sistema, incluyendo su directorio de inicio.
    with open('/etc/passwd') as file:
        for line in file:
            home_dir = line.split(':')[5]
            print(home_dir)

print("Listado de directorios:")
print_directory()

print("\n-------------------------------------------------------------- EJERCICIO 14 --------------------------------------------------------------")
# Implemente un script en Python, utilizando el módulo os, que liste todos los ficheros del directorio actual junto a su tamaño en bytes.
# Por último, el script mostrará la suma total del tamaño de los ficheros del directorio.
# Se deben incluir, además, los ficheros existentes en subdirectorios.

def print_current_directory():
    total_size = 0  # Inicializamos la variable que acumulará el tamaño total de los archivos

    for root, dirs, files in os.walk(".", topdown = False):  # Recorremos todos los archivos y subdirectorios a partir del directorio actual
        for name in files:  # Recorremos los archivos del directorio actual y los subdirectorios
            path = os.path.join(root, name)  # Obtenemos la ruta completa del archivo
            size = os.path.getsize(path)  # Obtenemos el tamaño del archivo en bytes
            total_size += size  # Sumamos el tamaño del archivo a la variable total_size
            print(f"{path}: {size} bytes")  # Imprimimos el nombre del archivo y su tamaño en bytes

    print(f"Total size: {total_size} bytes")  # Imprimimos el tamaño total de todos los archivos

print("Listado del directorio actual y sus subdirectorios:")
print_current_directory()

print("\n-------------------------------------------------------------- EJERCICIO 15 --------------------------------------------------------------")
# Realice un script en Python que mueva al directorio actual, todos los archivos contenidos en subdirectorios del mismo.
# Tenga en cuenta que un directorio puede contener a su vez otros directorios
# y que la longitud en la jerarquía del árbol no está definida y por tanto,
# el script debe funcionar para todos los casos.

def move_to_current_directory():
    ruta = "/home/jggomeztocino/CarpetaCopia"
    for root, dirs, files in os.walk(ruta, topdown=False):  # Recorremos todos los archivos y subdirectorios a partir del directorio actual
        for name in files:  # Recorremos los archivos del directorio actual y los subdirectorios
            src_path = os.path.join(root, name)  # Obtenemos la ruta completa del archivo
            dst_path = os.path.join(os.getcwd(), name)  # Obtenemos la ruta completa del destino
            shutil.move(src_path, dst_path)  # Movemos el archivo al directorio actual
            print(f"{src_path} movido a {dst_path}")  # Imprimimos el archivo movido y su destino

print("Resultado:")
move_to_current_directory()

print("\n-------------------------------------------------------------- EJERCICIO 16 --------------------------------------------------------------")
# Realizar un script en Python que imprima por pantalla el directorio de trabajo actual, junto a la lista de ficheros existentes en dicho directorio.
# Posteriormente, el mismo script permitirá al usuario renombrar un fichero.
# Para ello solicitará al usuario el nombre del fichero que quiere renombrar y el nuevo nombre que quiere darle.
# Se deben gestionar correctamente las posibles excepciones que puedan darse en la ejecución del script.

def rename():
    try:
        # Imprimimos el directorio de trabajo actual
        print(f"Directorio de trabajo actual: {os.getcwd()}")

        # Imprimimos la lista de ficheros existentes en el directorio actual
        print("Ficheros existentes en el directorio actual:")
        for file in os.listdir("."):
            if os.path.isfile(file):  # Nos aseguramos de que sea un archivo y no un directorio
                print(f"- {file}")

        # Pedimos al usuario el nombre del fichero a renombrar
        old_name = input("Introduce el nombre del fichero que quieres renombrar: ")

        # Pedimos al usuario el nuevo nombre del fichero
        new_name = input("Introduce el nuevo nombre del fichero: ")

        # Renombramos el fichero
        os.rename(old_name, new_name)
        print(f"El fichero {old_name} ha sido renombrado como {new_name}.")

    except FileNotFoundError:
        print("El fichero que quieres renombrar no existe en el directorio actual.")
    except FileExistsError:
        print("Ya existe un fichero con ese nombre en el directorio actual. Por favor, elige otro nombre.")
    except OSError as e:
        print(f"Error al renombrar el fichero: {e}")

rename()

print("\n-------------------------------------------------------------- EJERCICIO 17 --------------------------------------------------------------")
#  Realizar un script en Python que combine todos los ficheros de texto # (.txt) existentes en el directorio de trabajo actual
#  en un único fichero de texto, llamado “union.txt”.
#  Tanto los ficheros con una extensión distinta, como los que se encuentren en subdirectorios, deberán ignorarse.

def text_files_union():
    try:
        # Creamos un archivo nuevo llamado "union.txt"
        with open("union.txt", "w") as f_union:
            # Recorremos todos los ficheros del directorio actual
            for file in os.listdir("."):
                # Nos aseguramos de que sea un archivo de texto y no un directorio
                if os.path.isfile(file) and file.endswith(".txt"):
                    # Abrimos cada fichero de texto y lo leemos
                    with open(file, "r") as f:
                        content = f.read()
                    # Escribimos el contenido en el archivo "union.txt"
                    f_union.write(content)

        print("Los ficheros de texto han sido combinados en el archivo 'union.txt'.")

    except Exception as e:
        print(f"Error al combinar los ficheros de texto: {e}")


text_files_union()