def interseccion_listas(lista1, lista2):
    setLista = set(lista1) & set(lista2)
    return list(setLista)


if __name__ == 'main':
    lista1 = [1, 2, 3, 4]
    lista2 = [1, 3, 5, 7]
    print(interseccion_listas(lista1,lista2))