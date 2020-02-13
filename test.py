from parser import Parser
from graph import Graph
from tree import Tree
import os
import upit

i = 10
l = 0
lista_dokumenata=[]


def ucitaj_fajlove(file_path, graph, vertices):
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = file_path + "/" + fajl
        if os.path.isdir(putanja):
            ucitaj_fajlove(putanja, graph, vertices)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            vertices[putanja] = graph.insert_vertex(putanja)


def napravi_veze(vert, edg, graph, veritces):
    global i
    for v in edg:
        if v.endswith("html") or v.endswith("htm"):
            graph.insert_edge(vert, vertices[v], i)  # hash(vert) + hash(vertices[v]))
            i = i + 10


def ucitaj_fajlove2(file_path, trie, parser):
   # global lista_dokumenata

    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = file_path + "/" + fajl
        if os.path.isdir(putanja):
            ucitaj_fajlove2(putanja, trie, parser)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            parseHtml(file_path, trie, parser, fajl)
            lista_dokumenata.append(fajl)

def parseHtml(file_path, trie, parser, fajl):
    global l
    l = l + 1
    putanja = file_path + "/" + fajl
    ret = parser.parse(putanja)
    words = ret[1]
    for word in words:
        trie.add_word(word.lower(), fajl)


def proveri_postojanje(trie, word):
    if trie.does_word_exist(word.lower())[1] is None:
        print("Ne postoji ta rec!")

    else:
        lista = trie.does_word_exist(word)[1]
       # print(lista)
        # print(trie.find_word(word))
        lista1=trie.find_word(word)
        print(lista1)
        for elem in lista1:
            print(elem)
if __name__ == "__main__":
    parser = Parser()
    graph = Graph(True)
    trie = Tree()

    root = trie.root
    # trie.root=root

    vertices = {}
    radovanov_root = "/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html"
    aleksandrov_root = "/home/hal9000/OISISI_python_projekat/test-skup/python-2.7.7-docs-html/_images"
    string = upit.parsiraj_upit("not java")
    print("Izaberite korisnika:")
    print("1. Radovan")
    print("2. Aleksandar")
    print("3. Custom adress")
    adresa = input(">>>>>")
    if int(adresa) == 1:
        print("Ucitavanje za trie(1) ili ucitavanje za graph(2):")
        k = input(">>>>>>")
        if int(k) == 1:
            ucitaj_fajlove2(radovanov_root, trie, parser)
        elif int(k) == 2:
            ucitaj_fajlove(radovanov_root, graph, vertices)
        else:
            print("uneta je nepoznata vrednost!")

    elif int(adresa) == 2:
        print("Ucitavanje za trie(1) ili ucitavanje za graph(2):")
        k = input(">>>>>>")
        if int(k) == 1:
            ucitaj_fajlove2(aleksandrov_root, trie, parser)
            proveri_postojanje(trie,"python")
            while True:

                querry=input("Unesite upit:")
                print(querry)
                print(l)
                string = upit.parsiraj_upit(querry)
                print(string)
                doc_list = upit.upitaj(trie,string[1],string[2],string[0],lista_dokumenata)
                print(doc_list)


        elif int(k) == 2:
            ucitaj_fajlove(aleksandrov_root, graph, vertices)
        else:
            print("uneta je nepoznata vrednost!")
    elif int(adresa) == 3:
        print("Unesite adresu:")

        adresaCustom=input(">>>>>")
        ucitaj_fajlove(adresaCustom,graph,vertices)
    #
    # for element in graph.vertices():
    #     edg = parser.parse(str(element))
    #     napravi_veze(element, edg[0], graph, vertices)



        print("Ucitavanje za trie(1) ili ucitavanje za graph(2):")
        k = input(">>>>>>")

        if int(k) == 1:
            ucitaj_fajlove2(adresaCustom, root, parser)
        elif int(k) == 2:
            ucitaj_fajlove(adresaCustom, graph, vertices)
        else:
            print("uneta je nepoznata vrednost!")
    else:
        ret = parser.parse("/home/hal9000/OISISI_python_projekat/test-skup/python-2.7.7-docs-html/faq/index.html")
        reci = ret[1]
        for rec in reci:
            trie.add_word(rec.lower(), "index.html")

        # if (trie.does_word_exist("123456789")):

        ret1 = parser.parse("/home/hal9000/OISISI_python_projekat/test-skup/python-2.7.7-docs-html/faq/gui.html")
        reci1 = ret1[1]
        for rec in reci1:
            trie.add_word(rec.lower(), "gui.html")


        proveri_postojanje(trie, "123345324")
        proveri_postojanje(trie, "is")


    """
    for element in graph.vertices():
        edg = parser.parse(str(element))
        napravi_veze(element, edg[0], graph, vertices)

    #   trie.preorder(trie.root)
    #
    # for element in graph.vertices():
    #     edg = parser.parse(str(element))
    #     napravi_veze(element, edg[0], graph, vertices)

    # print(graph.get_edge(vertices["/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/genindex-K.html"], vertices["/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/library/curses.html"]))

    (outgoing, incoming) = graph.get_edges(vertices["/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/genindex-K.html"])
    for o in outgoing:
        print(str(o))
    e = parser.parse("/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/genindex-K.html")
    print(e[0])
    print(outgoing)
    print(incoming)
    for i in incoming:
        print(str(i))
    print(graph.vertex_count())
    print(graph.edge_count())
"""
