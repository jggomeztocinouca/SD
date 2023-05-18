def dict_add(mydict, t):
    if t is None:
        raise TypeError("El elemento es nulo")
    if len(t) != 2:
        raise TypeError("El elemento no es tupla")
    clave, valor = t
    mydict[clave] = valor
    return mydict


if __name__ == 'main':
    # La invocacion dict_add({1: 'manzana'}, {2, 'fresa'})} debera devolver como resultado {1: 'manzana', 2: 'fresa'}.
    mydict = {1: 'manzana'}
    t = (2, 'fresa')
    print(dict_add(mydict, t))
