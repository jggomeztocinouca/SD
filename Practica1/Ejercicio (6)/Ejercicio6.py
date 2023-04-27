def list_del(mylist, e):
    if e is None:
        raise TypeError("El elemento no puede ser nulo")
    if len(mylist) == 0:
        raise ValueError("La lista no puede ser vacía")

    mylist.remove(e)
    return mylist


if __name__ == "__main__":
    mylist = [5, 2, 4]
    print(list_del(mylist, 2))
