from lista import lista_bez_duplikata


def and_op(lista1, lista2): # sve elementi koji su u obe liste
    ret_lista = lista_bez_duplikata()
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                ret_lista.append(elem1)

    return ret_lista


def or_op(lista1, lista2): # svi elementi iz prve i druge liste
    ret_lista = lista_bez_duplikata()
    for elem1 in lista1:
        ret_lista.append(elem1)
    for elem2 in lista2:
        ret_lista.append(elem2)
    return ret_lista


def comp_op(lista1, lista2):  # svi elementi prve liste koji se ne poklapaju ni sa jednim lementom druge liste (prva i ne druga lista)
    ret = lista_bez_duplikata()

    for elem in lista1:
        ret.append(elem)

    for elem1 in ret:
        for elem2 in lista2:
            if elem1 == elem2:
                ret.remove(elem1)
    return ret
