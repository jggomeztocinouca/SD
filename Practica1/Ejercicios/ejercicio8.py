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
