from Skupovi.lista import Lista_bez_duplikata


def and_op(lista1, lista2):  # sve elementi koji su u obe liste

    if lista1 is not None and lista2 is not None:
        ret_lista = Lista_bez_duplikata()
        for elem1 in lista1:
            for elem2 in lista2:
                if elem1 == elem2:
                    ret_lista.append(elem1)
    else:
        ret_lista = None

    return ret_lista


def or_op(lista1, lista2):  # svi elementi iz prve i druge liste
    if lista1 is None and lista2 is not None:
        ret_lista = lista2
    elif lista1 is not None and lista2 is None:
        ret_lista = lista1
    elif lista1 is not None and lista2 is not None:
        ret_lista = Lista_bez_duplikata()
        for elem1 in lista1:
            ret_lista.append(elem1)
        for elem2 in lista2:
            ret_lista.append(elem2)
    else:
        ret_lista = None
    return ret_lista


def comp_op(lista1,
            lista2):  # svi elementi prve liste koji se ne poklapaju ni sa jednim lementom druge liste (prva i ne druga lista)
    ret = Lista_bez_duplikata()
    if lista1 is not None:
        for elem in lista1:
            ret.append(elem)
        if lista2 is not None:
            for elem1 in ret:
                for elem2 in lista2:
                    if elem1 == elem2:
                        ret.remove(elem1)
        else:
            for elem in lista1:
                ret.append(elem)
    else:
        ret = None
    return ret
