from collections import Counter

from Skupovi import skupovne_operacije
from Skupovi.lista import Lista_bez_duplikata


def parse(upit):
    upit = upit.lower()
    words = upit.split()
    bin1 = ""
    bin2 = ""
    i = 0
    if len(words) > 3:
        for word in words:
            if word == "not" or word == "and" or word == "or":
                i = -42
                bin1 = ""
                bin2 = ""
                return i, bin1, bin2

        bin1 = "1"
        bin2 = upit.lower()
        i = 4
        return i, bin1, bin2
    # ukoliko se upit sastorji iz 3 reci i bas srednja je "not", "and", "or",
    elif len(words) == 3:
        k = 1
        for word in words:
            if word == "not" or word == "and" or word == "or":
                k = 0

        if k == 0:
            if words[1] == "not":
                if words[0] != "not" and words[0] != "and" and words[0] != "or" and words[2] != "not" and words[2] != "and" and words[2] != "or":
                    i = 0
                    bin1 = words[0]
                    bin2 = words[2]
                else:
                    i = -42
            elif words[1] == "and":
                if words[0] != "not" and words[0] != "and" and words[0] != "or" and words[2] != "not" and words[2] != "and" and words[2] != "or":
                    i = 1
                    bin1 = words[0]
                    bin2 = words[2]
                else:
                    i = -42
            elif words[1] == "or":
                if words[0] != "not" and words[0] != "and" and words[0] != "or" and words[2] != "not" and words[2] != "and" and words[2] != "or":
                    i = 2
                    bin1 = words[0]
                    bin2 = words[2]
                else:
                    i = -42
            else:
                i = -42

            return i, bin1, bin2
        else:
            bin1 = "1"
            bin2 = upit.lower()
            i = 4
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
            bin1 = ""
            bin2 = ""
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
        ret_list = Lista_bez_duplikata()
        ret_map = None
    # 0 = not
    elif i == 0:
        if bin1 == "0":
            lista2 = tree.does_word_exist(bin2)[1]

            ret_list = skupovne_operacije.comp_op(lista, lista2)
            ret_map = {}

            if ret_list is not None:
                if ret_list.nmb_of_element() == 0:
                    ret_list = None
                else:
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
                if ret_list.nmb_of_element() == 0:
                    ret_list = None
                else:
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


        if bin1 == bin2:
            dif = mapa1
        else:
            a = mapa1.keys()

            set1 = []
            set2 = []

            b = mapa2. keys()

            for elem in a:
                set1.append(elem)

            for elem in b:
                set2.append(elem)

            konacni_set = []

            for elem in set1:
                if set2.__contains__(elem):
                    konacni_set.append(elem)

            # dif = {k: mapa1.get(k, 0) + mapa2.get(k, 0) for k in set(mapa1) & set(mapa2)}

            dif = {k: mapa1.get(k, 0) + mapa2.get(k, 0) for k in konacni_set}

        ret_list = skupovne_operacije.and_op(lista1, lista2)

        new_dict = {}
        if ret_list is not None:
            if ret_list.nmb_of_element() == 0:
                ret_list = None
            else:
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

        if bin1 == bin2:
            z = mapa1
        else:
            z = dict(Counter(mapa1) + Counter(mapa2))

        ret_list = skupovne_operacije.or_op(lista1, lista2)
        if ret_list is not None:
            if ret_list.nmb_of_element() == 0:
                ret_list = None

        ret_map = z

    # samo jedna rec u upitu
    elif i == 3:
        find = tree.does_word_exist(bin1)
        ret_list = find[1]
        help = find[2]
        if ret_list is not None:
            if ret_list.nmb_of_element() != 0:
                for key in help.keys():
                    if help[key] != 0:
                        ret_map[key] = help[key]
            else:
                ret_list = None
                ret_map = None

    elif i == 4:
        words = bin2.split()
        pomocna = []
        mape = []
        for word in words:
            find = tree.does_word_exist(word)
            if find[1] is not None:
                if find[1].nmb_of_element() != 0:
                    pomoc = find[1].set_to_list()
                    pomocna.append(pomoc)
                    mape.append(find[2])

        lista1 = None
        lista2 = None
        if len(pomocna) > 2:
            lista1 = list_to_set(pomocna[0])
            lista2 = list_to_set(pomocna[1])

            ret_list = skupovne_operacije.or_op(lista1, lista2)
            ret_map = dict(Counter(mape[0]) + Counter(mape[1]))

            for i in range(2, len(pomocna)):
                pomoc = list_to_set(pomocna[i])
                ret_list = skupovne_operacije.or_op(ret_list, pomoc)
                ret_map = dict(Counter(mape[i]) + Counter(ret_map))
        elif len(pomocna) == 2:
            lista1 = list_to_set(pomocna[0])
            lista2 = list_to_set(pomocna[1])

            ret_list = skupovne_operacije.or_op(lista1, lista2)
            ret_map = dict(Counter(mape[0]) + Counter(mape[1]))

        elif len(pomocna) == 1:
            ret_list = list_to_set(pomocna[0])
            ret_map = mape[0]
        else:
            ret_list = None
            ret_map = None
    return ret_list, ret_map


def list_to_set(lista):
    ret = Lista_bez_duplikata()
    for elem in lista:
        ret.append(elem)
    return ret
