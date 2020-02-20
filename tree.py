from queue import Queue

from lista import Lista_bez_duplikata
from treeNode import TreeNode


class Tree(object):

    def __init__(self, mapa):
        self.root = TreeNode("*", mapa)

    # dodavanje reci u stablo
    def add_word(self, word, origin_file, mapa):
        torka = self.does_word_exist(word)
        files = torka[1]
        mapa = torka[2]

        # ukoliko je does_word_exist vratio None, znaci da rec ne postoji! onda napravim set fajlova

        if files is None:
            files = Lista_bez_duplikata()

        if torka[0] is True:
            # ukoliko rec postoji samo se uveca za 1 broj ponavljanja i dodaje se u set fajlova koji sadrze tu rec

            files.add_element(origin_file)
            value1 = mapa[origin_file]
            mapa[origin_file] = value1 + 1
            return

        curr_node = self.root

        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TreeNode(letter, mapa)

            curr_node = curr_node.children[letter]

        # postavljanje vrednosti na kraj reci

        curr_node.is_end_of_word = True
        files.add_element(origin_file)
        curr_node.originFile = files

        # posto je broj ponavljanja u startu 0, samo se uvecava

        value = mapa[origin_file]
        curr_node.ponavljanje[origin_file] = value + 1

    # provera postojanja reci
    def does_word_exist(self, word):

        curr_node = self.root
        node = self.root
        for letter in word:
            if letter not in curr_node.children:
                # ukoliko ne postoji jedno od slova odmah iskace

                return False, None, node.ponavljanje
            curr_node = curr_node.children[letter]

        # ukoliko nije iskocio iz funkcije znaci da je nasao
        return True, curr_node.originFile, curr_node.ponavljanje

    def __iter__(self):
        to_visit = Queue()
        to_visit.enqueue(self.root)
        while not to_visit.is_empty():
            e = to_visit.dequeue()
            yield e

            for c in e.children:
                to_visit.enqueue(c)
