def union_listas(lista1, lista2):
    set(lista1)
    set(lista2)
    return set(lista1 + lista2)


if __name__ == 'main':
    lista1 = [1, 2, 3, 4]
    lista2 = [1, 3, 5, 7]
    print(union_listas(lista1, lista2))
