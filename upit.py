import skupovne_operacije
from lista import lista_bez_duplikata


def parsiraj_upit(upit):
    words = upit.split()
    i=-1
    bin1=""
    bin2=""
    if len(words) == 1:
        i=3
        bin1 = upit
        bin2 = "0"
    for j in range(len(words)):
        word = words[j]
        if word.lower() == "not":
            i = 0
            if j == 0 :
                bin1 = "0"
            else:
                bin1 = words[j-1]

            bin2 = words[j+1]
        elif word.lower() == "and":
            i = 1
            bin1 = words[j - 1]
            bin2 = words[j + 1]
        elif word.lower() == "or":
            i=2
            bin1 = words[j - 1]
            bin2 = words[j + 1]

    if i == -1:
        bin1 = words[0]
        bin2 = words[1]
        i = 2

    return i,bin1,bin2
def upitaj(tree,bin1,bin2,i,lista):
    #print(lista)
    ret_list = []
    if i == 0:
        if bin1 == "0":
            lista2 = tree.find_word(bin2)
            ret_list = skupovne_operacije.comp_op(lista,lista2)
        else:
            lista1 = tree.find_word(bin1)
            lista2 = tree.find_word(bin2)
            ret_list = skupovne_operacije.comp_op(lista1,lista2)
    elif i == 1:
        lista1 = tree.find_word(bin1)
        lista2 = tree.find_word(bin2)
        #print(lista1,lista2)
        ret_list=skupovne_operacije.and_op(lista1,lista2)
    elif i == 2:
        lista1 = tree.find_word(bin1)
        print(lista1)
        lista2 = tree.find_word(bin2)
        print(lista2)
        ret_list = skupovne_operacije.or_op(lista1, lista2)
    elif i == 3:
        ret_list = tree.find_word(bin1)

    return ret_list