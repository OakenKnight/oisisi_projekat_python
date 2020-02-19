from collections import Counter

import skupovne_operacije
from lista import lista_bez_duplikata


def parse(upit):
    words = upit.split()
    bin1 = ""
    bin2 = ""
    i = 0
    if len(words) == 3:
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

    elif len(words) == 2:
        if words[0] == "not":
            if words[1] != "not":
                bin1 = "0"
                i = 0
                bin2 = words[1]
            else:
                i = -42
                bin1 = ""
                bin2 = ""
            return i, bin1, bin2

        for word in words:
            if word == "and" or word == "or":
                i = -42
                bin1 = ""
                bin2 = ""
                return i, bin1, bin2
        bin1 = words[0]
        bin2 = words[1]
        i = 2
        return i, bin1, bin2

    elif len(words) == 1:
        bin1 = words[0]
        bin2 = ""
        i = 3
        return i, bin1, bin2
    else:
        i = -42
        bin1 = ""
        bin2 = ""
        return i, bin1, bin2


def upitaj(tree, bin1, bin2, i, lista):
    # print(lista)
    ret_list = lista_bez_duplikata()
    occur_map1 = {}
    occur_map2 = {}
    if i == -42:
        print("Greska! Nije uneseno u dobrom formatu!")
        ret_list = None
        ret_map = None
    elif i == 0:
        if bin1 == "0":
            lista2 = tree.does_word_exist(bin2)[1]
            # occur_map1 = torka[1]
            # occur_map2={}
            ret_list = skupovne_operacije.comp_op(lista, lista2)
            ret_map = {}
            for elem in ret_list:
                ret_map[elem] = 42
        else:
            lista1 = tree.does_word_exist(bin1)[1]
            lista2 = tree.does_word_exist(bin2)[1]
            map1 = tree.does_word_exist(bin1)[2]
            # occur_map1 = torka1[1]
            # occur_map2 = torka2[1]

            ret_list = skupovne_operacije.comp_op(lista1, lista2)
            ret_map = {}

            for elem in ret_list:
                ret_map[elem] = map1[elem]

    elif i == 1:
        lista1 = tree.does_word_exist(bin1)[1]
        lista2 = tree.does_word_exist(bin2)[1]
        mapa = tree.does_word_exist(bin1)[2]
        mapa2 = tree.does_word_exist(bin2)[2]
        suma = 0
        #
        # for elem in mapa.keys():
        #     if mapa[elem] != 0:
        #         print(elem, mapa[elem])
        #         suma += 1
        # #
        # print("Nesto drugo")
        # for elem in mapa2.keys():
        #     if mapa2[elem] != 0:
        #         print(elem, mapa2[elem])
        #         suma += 1
        # occur_map1 = torka1[1]
        # occur_map2 = torka2[1]
        # print(suma)
        # z = dict(Counter(mapa) + Counter(mapa2))
        # print(z)
        dif={k: mapa.get(k, 0) + mapa2.get(k, 0) for k in set(mapa) & set(mapa2)}
       # print(dif)
        for elem in dif.keys():
            if dif[elem] != 0:
                 print(elem,dif[elem])
        ret_list = skupovne_operacije.and_op(lista1, lista2)
        new_dict = {}
        for elem in ret_list:
            new_dict[elem] = dif[elem]

        #print(new_dict)
        ret_map = new_dict
    elif i == 2:
        lista1 = tree.does_word_exist(bin1)[1]
        lista2 = tree.does_word_exist(bin2)[1]
        mapa = tree.does_word_exist(bin1)[2]
        mapa2 = tree.does_word_exist(bin2)[2]
        #print(" ####" , mapa2)
        #print(" #### ####" ,mapa)
        suma = 0
        for elem in mapa.keys():
            if mapa[elem] != 0:
                print(elem,mapa[elem])
                suma += 1
        #
        #print("Nesto drugo")
        for elem in mapa2.keys():
            if mapa2[elem] !=0:
                print(elem, mapa2[elem])
                suma += 1
        # occur_map1 = torka1[1]
        # occur_map2 = torka2[1]
        #print(suma)
        z=dict(Counter(mapa) + Counter(mapa2))
        #print(z)
        ret_list = skupovne_operacije.or_op(lista1, lista2)
        ret_map = z
    elif i == 3:
        ret_list = tree.does_word_exist(bin1)[1]
        help = tree.does_word_exist(bin1)[2]
        ret_map={}
        for key in help.keys():
            if help[key] != 0:
                ret_map[key] = help[key]
    return ret_list, ret_map # , occur_map1, occur_map2
