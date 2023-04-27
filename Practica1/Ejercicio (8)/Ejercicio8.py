def prime(a, b):
    if a is None or b is None:
        raise TypeError("Los elementos no pueden ser nulos")
    if type(a) is not int or type(b) is not int:
        raise TypeError("Los elementos deben ser enteros")
    primos = []
    for numero in range(a, b + 1):  # rango [a,b]. Si no hubiésemos puesto +1 sería [a,b)
        if numero > 1:
            for i in range(2, numero):  # Un numero es primo si sólo es divisible por 1 y la unidad
                if numero % i == 0:
                    break
            else:
                primos.append(numero)
    return primos


if __name__ == 'main':
    print(prime(2, 10))
