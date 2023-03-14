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

