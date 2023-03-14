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
