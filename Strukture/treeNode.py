from Skupovi.lista import Lista_bez_duplikata


class TreeNode(object):
    def __init__(self, letter, mapa):
        map = {}
        for elem in mapa.keys():
            map[elem] = 0

        self.letter = letter
        self.children = {}
        self.is_end_of_word = False
        self.originFile = Lista_bez_duplikata()
        self.ponavljanje = map

    def __str__(self):
        return str(self.letter)
