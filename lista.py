class lista_bez_duplikata():
    def __init__(self):
        self.list = []

    def check_element(self, element):
        for elem in self.list:
            if element == elem:
                return False

        return True

    def add_element(self, element):
        if self.check_element(element):
            self.list.append(element)

    def __str__(self):
        return str(self.list)

    def __setitem__(self, index, value):
        self.list[index] = value

    def __getitem__(self, index):
        return self.list[index]

    def __contains__(self, item):
        for elem in self.list:
            if elem == item:
                return False
        return True
    def append(self,item):
        if self.list.__contains__(item) is False:
            self.list.append(item)

    def copy(self):
        lista1 = lista_bez_duplikata()
        for item in self.list:
            lista1.append(item)

        return lista1
    def nmb_of_element(self):
        i = 0
        for elem in self.list:
            i += 1
        return i

    def remove(self,item):
        for elem in self.list:
            if elem == item:
                self.list.remove(elem)
