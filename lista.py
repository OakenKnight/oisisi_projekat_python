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

    def __iter__(self):
        for elem in self.list:
            yield elem


    def set_to_list(self):
