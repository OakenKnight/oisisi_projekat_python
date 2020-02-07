from parser import Parser
from graph import Graph
from tree import Tree
from treeNode import TreeNode
import os

i = 10

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
            graph.insert_edge(vert, vertices[v], i) #hash(vert) + hash(vertices[v]))
            i = i + 10


def ucitaj_fajlove2(file_path, root,parser):
    fajlovi=os.listdir(file_path)
    for fajl in fajlovi:
        putanja = file_path+"/"+fajl
        if os.path.isdir(putanja):
            ucitaj_fajlove2(putanja,root,parser)
        elif fajl.endswith("html"):
            parseHtml(file_path,root,parser,fajl)

def split(word):
    return [char for char in word]

def parseHtml(file_path,root , parser,fajl):
    putanja = file_path + "/" + fajl
    retVal=parser.parse(putanja)
    words= retVal[1]
    k=0
    i=0
    slovaDokumenta=[]
    while k < len(words):
        slovaDokumenta=split(words[k])

        ucvori(slovaDokumenta,fajl,root)

def ucvori(rec,fajl,root):
    i=len(rec)
    k=0
    while k < len(rec)-1:
        cvor=napraviCvor(rec[k])
        root.add_child(cvor)
        root=cvor
        k=k+1
    kraj=napraviCvor(rec[k],fajl)
    root.add_child(kraj)

def napraviCvor(slovo,fajl=None):
    data={slovo,fajl}
    cvor=TreeNode(data)
    return cvor

if __name__ == "__main__":
    parser = Parser()
    graph = Graph(True)
    trie = Tree()
    root = TreeNode(0)
    trie.root=root

    vertices = {}
    radovanov_root= "/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html"
    aleksandrov_root= "/home/hal9000/OISISI_python_projekat/test-skup/python-2.7.7-docs-html"
    print("Izaberite korisnika:")
    print("1. Radovan")
    print("2. Aleksandar")
    print("3. Custom adress")
    adresa=input(">>>>>")
    if int(adresa) == 1:
        print("Ucitavanje za trie(1) ili ucitavanje za graph(2):")
        k=input(">>>>>>")
        if int(k)==1:
            ucitaj_fajlove2(radovanov_root,root,parser)
        elif int(k) == 2:
            ucitaj_fajlove(radovanov_root,graph,vertices)
        else:
            print("uneta je nepoznata vrednost!")

    elif int(adresa) == 2:
        print("Ucitavanje za trie(1) ili ucitavanje za graph(2):")
        k = input(">>>>>>")
        if int(k) == 1:
            ucitaj_fajlove2(aleksandrov_root, root, parser)
        elif int(k) == 2:
            ucitaj_fajlove(aleksandrov_root, graph, vertices)
        else:
            print("uneta je nepoznata vrednost!")
    else:
        print("Unesite adresu:")
        adresaCustom=input(">>>>>")
        print("Ucitavanje za trie(1) ili ucitavanje za graph(2):")
        k = input(">>>>>>")
        if int(k) == 1:
            ucitaj_fajlove2(adresaCustom, root, parser)
        elif int(k) == 2:
            ucitaj_fajlove(adresaCustom, graph, vertices)
        else:
            print("uneta je nepoznata vrednost!")
    #ucitaj_fajlove("/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html", graph, vertices)


    for element in graph.vertices():
        edg = parser.parse(str(element))
        napravi_veze(element, edg[0], graph, vertices)


   # print(graph.get_edge(vertices["/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/genindex-K.html"], vertices["/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/library/curses.html"]))
    """"
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