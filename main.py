from parser import Parser
from graph import Graph
from tree import Tree
from treeNode import TreeNode
import os

i = 10
l = 0

def napravi_cvorove(file_path, graph, vertices):
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = file_path + "/" + fajl
        if os.path.isdir(putanja):
            napravi_cvorove(putanja, graph, vertices)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            vertices[putanja] = graph.insert_vertex(putanja)


def napravi_veze(vert, edg, graph, vertices):
    global i
    for v in edg:
        if v.endswith("html") or v.endswith("htm"):
            lok_adresa = str(v).split("/")
            v = "test-skup"
            prodji = False
            for l in lok_adresa:
                if prodji:
                    v = v + "/" + l
                if l == "test-skup":
                    prodji = True
            graph.insert_edge(vert, vertices[v], i)
            i = i + 10


def napravi_drvo(file_path, trie, parser):
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = file_path + "/" + fajl
        if os.path.isdir(putanja):
            napravi_drvo(putanja, trie, parser)
        elif fajl.endswith("html"):
            parseHtml(file_path, trie, parser, fajl)


def parseHtml(file_path, trie, parser, fajl):
    global l
    l = l + 1
    putanja = file_path + "/" + fajl
    ret = parser.parse(putanja)
    words = ret[1]
    for word in words:
        trie.add_word(word, fajl)


def proveri_postojanje(trie, word):
    if trie.does_word_exist(word)[1] is None:
        print("Ne postoji ta rec!")
    else:
        trie.find_word(word)



if __name__ == "__main__":

    parser = Parser()
    graph = Graph(True)
    vertices = {}
    petlja = True
    korenski_dir = "test-skup"
    while petlja:
            direktorijumi = os.listdir(korenski_dir)
            print("Dostupni direktorijumi:")
            i = 1
            poddirektorijumi = []
            for dir in direktorijumi:
                putanja = korenski_dir + "/" + dir
                if os.path.isdir(putanja):
                    poddirektorijumi.append(dir)
                    print(i, ".", dir)
                    i = i + 1
            if i == 1:
                print("#Trenutni direktorijum nema poddirektorijume.")
                print("1.Povratak u prethodni direktorijum\n2.Ostanak u trenutnom direktorijumu")
                unos = input(">>>>")
                if int(unos) == 1:
                    st = korenski_dir.split("/")
                    duzina_poslednjeg = len(st[len(st) - 1]) + 1
                    korenski_dir = korenski_dir[: -duzina_poslednjeg]
                    continue
                elif int(unos) == 2:
                    petlja = False
                    print("#Izabrali ste direktorijum: ", str(korenski_dir))
                    continue
            print("#Izaberite broj direktorijuma\n#Za povratak u prethodni direktorijum unesite -1\n#Za ostanak u trenutnom direktorijumu unesite 0")
            unos = input(">>>>")
            if int(unos) < i and int(unos) > 0:
                korenski_dir = str(korenski_dir) + "/" + poddirektorijumi[int(unos) - 1]
            elif int(unos) == -1:
                st = korenski_dir.split("/")
                if len(st) == 1:
                    print("Nalazite se u prvom direktorijumu!!!(Nema 'nadredjenih' direktorijuma)")
                    continue
                duzina_poslednjeg = len(st[len(st) - 1]) + 1
                korenski_dir = korenski_dir[: -duzina_poslednjeg]
                continue
            elif int(unos) == 0:
                print("#Izabrali ste direktorijum: ", str(korenski_dir))
                petlja = False
            else:
                print("#POGRESAN UNOS !!!")

    print("~~~Ucitavanje podataka~~~")
    if korenski_dir == 'test-skup':
        napravi_cvorove("test-skup", graph, vertices)
    else:
        dir = korenski_dir.split("/")
        napravi_cvorove("test-skup" + "/" + str(dir[1]), graph, vertices)

    for element in graph.vertices():
        edg = parser.parse(str(element))
        napravi_veze(element, edg[0], graph, vertices)
