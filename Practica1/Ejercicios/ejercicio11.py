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
