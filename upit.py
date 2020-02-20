from collections import Counter

import skupovne_operacije
from lista import lista_bez_duplikata


def parse(upit):
    words = upit.split()
    bin1 = ""
    bin2 = ""
    i = 0
    # ukoliko se upit sastorji iz 3 reci i bas srednja je "not", "and", "or",
    if len(words) == 3:
        if words[0] != "not" and words[0] != "and" and words[0] != "or" and words[2] != "not" and words[2] != "and" and \
                words[2] != "or":
            if words[1] == "not":
                i = 0
                bin1 = words[0]
                bin2 = words[2]
            elif words[1] == "and":
                i = 1
                bin1 = words[0]
                bin2 = words[2]
            elif words[1] == "or":
                i = 2
                bin1 = words[0]
                bin2 = words[2]
            else:
                i = -42

            return i, bin1, bin2

    # ukoliko se upit sastorji iz 2 reci
    elif len(words) == 2:
        # ukoliko je prva rec "not" onda druga mora da bude razlicita od  od bilo kog logickog operatora
        if words[0] == "not":
            if words[1] != "not" and words[1] != "and" and words[1] != "or":
                bin1 = "0"
                i = 0
                bin2 = words[1]
            else:
                i = -42
                bin1 = ""
                bin2 = ""
            return i, bin1, bin2
        # ako prva rec nije "not" proveravam da li je bilo koja od reci neki logicki operator
        for word in words:
            if word == "and" or word == "or" or word == "not":
                i = -42
                bin1 = ""
                bin2 = ""
                return i, bin1, bin2

        bin1 = words[0]
        bin2 = words[1]
        i = 2

        return i, bin1, bin2

    elif len(words) == 1:
        # proveravam ukoliko se upit sastoji iz jedne reci da li je to neka od logickih operatora
        if words[0] != "not" and words[0] != "and" and words[0] != "or":

            bin1 = words[0]
            bin2 = ""
            i = 3
            return i, bin1, bin2

        else:
            bin1=""
            bin2=""
            i = -42
            return i, bin1, bin2
    # ukoliko nije duzina upita 1 2 3 reci onda je greska
    else:
        i = -42
        bin1 = ""
        bin2 = ""
        return i, bin1, bin2


def upitaj(tree, bin1, bin2, i, lista):
    ret_list = None
    ret_map = {}
    if i == -42:
        print("Greska! Nije uneseno u dobrom formatu!")
        ret_list = lista_bez_duplikata()
        ret_map = None
    # 0 = not
    elif i == 0:
        if bin1 == "0":
            lista2 = tree.does_word_exist(bin2)[1]

            ret_list = skupovne_operacije.comp_op(lista, lista2)
            ret_map = {}

            for elem in ret_list:
                ret_map[elem] = 0

        else:
            find1 = tree.does_word_exist(bin1)
            find2 = tree.does_word_exist(bin2)

            lista1 = find1[1]
            mapa1 = find1[2]

            lista2 = find2[1]

            ret_list = skupovne_operacije.comp_op(lista1, lista2)
            ret_map = {}
            if ret_list is not None:
                for elem in ret_list:
                    ret_map[elem] = mapa1[elem]

    # 1 = and
    elif i == 1:
        find1 = tree.does_word_exist(bin1)
        find2 = tree.does_word_exist(bin2)

        lista1 = find1[1]
        mapa1 = find1[2]

        lista2 = find2[1]
        mapa2 = find2[2]

        #mozda popraviti
        dif = {k: mapa1.get(k, 0) + mapa2.get(k, 0) for k in set(mapa1) & set(mapa2)}

        ret_list = skupovne_operacije.and_op(lista1, lista2)
        new_dict = {}
        if ret_list is not None:
            for elem in ret_list:
                new_dict[elem] = dif[elem]

        ret_map = new_dict
    # 2 = or
    elif i == 2:

        find1 = tree.does_word_exist(bin1)
        find2 = tree.does_word_exist(bin2)

        lista1 = find1[1]
        mapa1 = find1[2]

        lista2 = find2[1]
        mapa2 = find2[2]

        z = dict(Counter(mapa1) + Counter(mapa2))

        ret_list = skupovne_operacije.or_op(lista1, lista2)
        ret_map = z
    # samo jedna rec u upitu
    elif i == 3:
        find = tree.does_word_exist(bin1)
        ret_list = find[1]
        help = find[2]

        for key in help.keys():
            if help[key] != 0:
                ret_map[key] = help[key]

    return ret_list, ret_map
