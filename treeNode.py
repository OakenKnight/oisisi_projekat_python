from lista import lista_bez_duplikata


class TreeNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False
        self.originFile = lista_bez_duplikata()
        self.occurnace = {}

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0

    def add_child(self, x):
        x.parent = self
        self.children.append(x)

    def __str__(self):
        return str(self.letter)
