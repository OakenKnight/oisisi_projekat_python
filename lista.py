class lista_bez_duplikata(object):
    def __init__(self):
        self.list = []

    def check_element_existance(self, element):
        for elem in self.list:
            if element == elem:
                return False

        return True

    def add_element(self, element):
        if self.check_element_existance(element):
            self.list.append(element)

    def __str__(self):
        return str(self.list)

    def  and_op(self, lista1, lista2):
        ret_lista = []
        for elem1 in lista1:
            for elem2 in lista2:
                if elem1 == elem2 and not ret_lista.__contains__(elem1):
                    ret_lista.append(elem1)

        return ret_lista

    def or_op(self, lista1, lista2):
        ret_lista = []
        for elem1 in lista1:
            if  not ret_lista.__contains__(elem1):
                ret_lista.append(elem1)
        for elem2 in lista2:
            if  not ret_lista.__contains__(elem2):
                ret_lista.append(elem2)
        return ret_lista

    def comp_op(self, lista1, lista2):      #svi elementi prve liste koji se ne poklapaju ni sa jednim lementom druge liste
        ret_lista = lista1.copy()
        for elem1 in lista1:
            for elem2 in lista2:
                if elem1 == elem2:
                    if ret_lista.__contains__(elem1):
                        ret_lista.remove(elem1)
        ret_lista = list(dict.fromkeys(ret_lista))
        return ret_lista

