def list_add(mylist, e):
    if e is None:
        raise TypeError("No se puede añadir un elemento nulo")
    mylist.append(e)
    return mylist


if __name__ == 'main':
    mylist = [5, 2, 4]
    print(list_add(mylist, 2))
