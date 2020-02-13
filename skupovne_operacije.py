from lista import lista_bez_duplikata
import copy

def and_op(lista1, lista2):
    ret_lista = lista_bez_duplikata()
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2 and not ret_lista.__contains__(elem1):
                ret_lista.append(elem1)

    return ret_lista


def or_op(lista1, lista2):
    ret_lista = []
    for elem1 in lista1:
        if not ret_lista.__contains__(elem1):
            ret_lista.append(elem1)
    for elem2 in lista2:
        if not ret_lista.__contains__(elem2):
            ret_lista.append(elem2)
    return ret_lista


def comp_op(lista1, lista2):  # svi elementi prve liste koji se ne poklapaju ni sa jednim lementom druge liste (prva i ne druga lista)
    ret_lista = lista1.copy()
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                ret_lista.remove(elem1)
    return ret_lista