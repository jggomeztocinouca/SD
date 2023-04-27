def accum(x, y, z):
    if not type(x) == int or not type(y) == int or not type(z):
        raise TypeError("Los argumentos deben ser enteros")
    suma = 0
    if x%2 == 0:
        suma += x
    if y%2 == 0:
        suma += y
    if z%2 == 0:
        suma += z

    return suma

if __name__ == 'main':
    suma = accum(5, 4, 2)
    print(suma)