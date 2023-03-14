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
