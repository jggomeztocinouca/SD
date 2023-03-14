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
