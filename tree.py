from queue import Queue
from treeNode import TreeNode
from lista import lista_bez_duplikata


class Tree(object):

    def __init__(self):
        self.root = TreeNode("*")

    def add_word(self, word, origin_file):
        torka = self.does_word_exist(word)
        files = torka[1]
        if files is None:
            files = lista_bez_duplikata()

        if torka[0] is True:  # znaci da postoji ta rec vec
            files.add_element(origin_file)

            return

        curr_node = self.root

        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TreeNode(letter)

            curr_node = curr_node.children[letter]

        curr_node.is_end_of_word = True
        files.add_element(origin_file)
        curr_node.originFile = files

    def does_word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False, None
            curr_node = curr_node.children[letter]

        return True, curr_node.originFile

    def find_word(self, word):
        curr_node = self.root
        lista = lista_bez_duplikata()

        for letter in word:
            if letter not in curr_node.children:
                break

            curr_node = curr_node.children[letter]
        if curr_node.is_end_of_word is True:
            lista = curr_node.originFile
            return lista
        return lista

    def is_empty(self):
        return self.root is None

    def depth(self, x):
        if x.is_root():
            return 0
        else:
            return 1 + self.depth(x.parent)

    def __iter__(self):
        to_visit = Queue()
        to_visit.enqueue(self.root)
        while not to_visit.is_empty():
            e = to_visit.dequeue()
            yield e

            for c in e.children:
                to_visit.enqueue(c)


""""
    def add_word(self, word, origin_file):

        torka=self.does_word_exist(word)
        files=torka[1]
        ocur=torka[2]
        if files is None:
            files = lista_bez_duplikata()
            #orig = '"' + origin_file + '"'
            ocur[origin_file] = 0
        if torka[0] is True: #znaci da postoji ta rec vec
            files.add_element(origin_file)
            # orig='"'+origin_file+ '"'
            #
            val = ocur[origin_file]
            ocur[origin_file] = val+1
            return

        curr_node = self.root

        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TreeNode(letter)

            curr_node = curr_node.children[letter]

        curr_node.is_end_of_word = True
        files.add_element(origin_file)
        curr_node.originFile = files
        # orig = '"' + origin_file + '"'
        #
        val = ocur[origin_file]
        ocur[origin_file] = val + 1
    
    def does_word_exist(self, word):
        curr_node = self.root
        #lista = lista_bez_duplikata()
        for letter in word:
            if letter not in curr_node.children:
                return False, None , {}
            curr_node = curr_node.children[letter]

        return  True,curr_node.originFile , curr_node.occurnace
    
    def find_word(self, word):
        curr_node = self.root
        lista=lista_bez_duplikata()
        empty_occur={}
        for letter in word:
            if letter not in curr_node.children:
                break

            curr_node = curr_node.children[letter]
        if curr_node.is_end_of_word is True:
            lista = curr_node.originFile
            occurance = curr_node.occurnace
            print(occurance)
            print(lista)
            return lista, occurance
        return lista, empty_occur

    """
