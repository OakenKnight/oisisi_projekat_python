import upit
from parser import Parser
from graph import Graph
from tree import Tree
from treeNode import TreeNode
import os
from sort import quick_sort


i = 10
l = 0
lista_dokumenata = []  # moze da se ubaci u main i da se odatle poziva


def napravi_cvorove(file_path, graph, vertices):
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = os.path.join(file_path, fajl)
        if os.path.isdir(putanja):
            napravi_cvorove(putanja, graph, vertices)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            vertices[putanja] = graph.insert_vertex(putanja)


def napravi_veze_i_drvo(file_path, graph, vertices, parser, trie, lista_dokumenata):
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = os.path.join(file_path, fajl)
        if os.path.isdir(putanja):
            napravi_veze_i_drvo(putanja, graph, vertices, parser, trie, lista_dokumenata)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            parseHtml(file_path, trie, parser, fajl, vertices, graph)
            lista_dokumenata.append(putanja)


def napravi_veze(vert, edg, graph, vertices):
    global i
    for v in edg:
        if v.endswith("html") or v.endswith("htm"):
            if "/" in os.path.abspath(v):
                slash = "/"
            elif "\\" in os.path.abspath(v):
                slash = "\\"
            else:
                print("Nesto nije u redu sa adresom!!!")
                print("Veze u grafu nisu uspesno napravljene!!!")
            lok_adresa = str(v).split(slash)
            v = "test-skup"
            prodji = False
            for l in lok_adresa:
                if prodji:
                    v = os.path.join(v, l)
                if l == "test-skup":
                    prodji = True
        if vertices.__contains__(v):
            graph.insert_edge(vert, vertices[v], i)
            i = i + 10


# def napravi_drvo(file_path, trie, parser):
#     global lista_dokumenata
#
#     fajlovi = os.listdir(file_path)
#     for fajl in fajlovi:
#        # putanja = file_path + "/" + fajl
#         putanja1=os.path.join(file_path, fajl)
#         #print(putanja1)
#         if os.path.isdir(putanja1):
#             napravi_drvo(putanja1, trie, parser)
#
#         elif fajl.endswith("html") or fajl.endswith("htm"):
#             parseHtml(file_path, trie, parser, fajl)
#             lista_dokumenata.append(putanja1)

def parseHtml(file_path, trie, parser, fajl, vertices, graph):
    global l
    l = l + 1
    putanja1 = os.path.join(file_path, fajl)
    ret = parser.parse(putanja1)
    links = ret[0]
    napravi_veze(vertices[putanja1], links, graph, vertices)
    words = ret[1]
    for word in words:
        trie.add_word(word.lower(), putanja1)


def proveri_postojanje(trie, word):
    if trie.does_word_exist(word)[1] is None:
        print("Ne postoji ta rec!")
    else:
        lista = trie.find_word(word.lower())
        print(lista)


def postoji_direktorijum(file_path):
    if os.path.isdir(file_path):
        return True
    else:
        return False


def rucno_unos_direktorijuma():
    print("Za unos relativne adrese u odnosu na 'test-skup' unesite 1")
    print("Za odabir jednog od ponudjenih direktorijuma iz 'test-skup' direktorijuma unesite 2")
    unos = input(">>>>")
    adresa = ""
    if int(unos) == 1:
        petlja = True
        while petlja:
            print("Unesite adresu(npr. test-skup/.../.../...):")
            adresa = input(">>>>")
            if "test-skup" in adresa:
                if postoji_direktorijum(adresa):
                    petlja = False
                else:
                    print("Zeljena adresa ne postoji kao poddirektorijum 'test-skup' direktorijuma")
            else:
                adresa = os.path.join("test-skup", adresa)
                if postoji_direktorijum(adresa):
                    petlja = False
                else:
                    print("Zeljena adresa ne postoji kao poddirektorijum 'test-skup' direktorijuma")
                    print("Proverite da li ste ispravno uneli adresu")
        return True, adresa
    elif int(unos) == 2:
        return False, ""


def izaberi_direktorijum():
    (rucno, korenski_dir) = rucno_unos_direktorijuma()
    if rucno:
        return korenski_dir
    else:
        petlja = True
        korenski_dir = "test-skup"
        if "/" in os.path.abspath("test-skup"):
            slash = "/"
        elif "\\" in os.path.abspath("test-skup"):
            slash = "\\"
        else:
            print("Nesto ne valja sa adresom!!!")
        while petlja:
            direktorijumi = os.listdir(korenski_dir)
            print("Dostupni direktorijumi:")
            i = 1
            poddirektorijumi = []
            for dir in direktorijumi:
                putanja = os.path.join(korenski_dir, dir)
                if os.path.isdir(putanja):
                    poddirektorijumi.append(dir)
                    print(i, ".", dir)
                    i = i + 1
            if i == 1:
                print("#Trenutni direktorijum nema poddirektorijume.")
                print(
                    "#Za povratak u prethodni direktorijum unesite 1\n#Za ostanak u trenutnom direktorijumu unesite 2")
                unos = input(">>>>")
                try:
                    uneseno = int(unos)
                except ValueError:
                    print("Nije unesen broj! Molimo Vas pokusajte ponovo!")
                    continue
                if uneseno == 1:
                    st = korenski_dir.split(slash)
                    duzina_poslednjeg = len(st[len(st) - 1]) + 1
                    korenski_dir = korenski_dir[: -duzina_poslednjeg]
                    continue
                elif uneseno == 2:
                    petlja = False
                    print("#Izabrali ste direktorijum: ", str(korenski_dir))
                    continue
            print(
                "#Izaberite broj direktorijuma\n#Za povratak u prethodni direktorijum unesite -1\n#Za ostanak u trenutnom direktorijumu unesite 0")
            unos = input(">>>>")
            try:
                uneseno = int(unos)
            except ValueError:
                print("Nije unesen broj! Molimo Vas pokusajte ponovo!")
                continue

            if uneseno < i and uneseno > 0:
                korenski_dir = os.path.join(str(korenski_dir), poddirektorijumi[int(unos) - 1])
            elif uneseno == -1:
                st = korenski_dir.split(slash)
                if len(st) == 1:
                    print("Nalazite se u prvom direktorijumu!!!(Nema 'nadredjenih' direktorijuma)")
                    continue
                duzina_poslednjeg = len(st[len(st) - 1]) + 1
                korenski_dir = korenski_dir[: -duzina_poslednjeg]
                continue
            elif uneseno == 0:
                print("#Izabrali ste direktorijum: ", str(korenski_dir))
                petlja = False
            else:
                print("#Nepostojeca komanda !!!")
        return korenski_dir

def promena_n():
    while True:
        print("Koliko stranica zelite da se prikaze odjednom(ceo broj):")
        unos = input(">>>>")
        if int(unos) < 1:
            print("Nemoguce je prikazati manje od 1 stranice!!!")
        else:
            return int(unos)

def ispis(doc,i):
    (outc, inc) = graph.get_edges(vertices[doc])
    print(i, ".", doc)
    print("\t\t-Broj stranica koje pokazuju na ovu stranicu:", len(inc))
    print("\t\t-Broj stranica na koje pokazuje ova stranica:", len(outc))

def prikaz_rezultata(n,doc_list):
    petlja = True
    unos = 1
    broj_stranica = int(doc_list.nmb_of_element()/n + 0.999)
    print(broj_stranica)
    while petlja:
        for i in range((int(unos) - 1) * n, int(unos) * n):
            if i < doc_list.nmb_of_element():
                ispis(doc_list[i], i + 1)
        print(">", end=" ")
        if broj_stranica < 11:
            for i in range(1, broj_stranica + 1):
                print(i, end=" ")
        else:
            for i in range(1, broj_stranica + 1):
                if i < 6:
                    print(i, end=" ")
                elif i == 6:
                    print("...", end=" ")
                else:
                    for j in range(broj_stranica - 4, broj_stranica + 1):
                        print(j, end=" ")
                    break

        print("<", end=" ")
        print("\n1 - Promena stranice:")
        print("2 - Pretrazi sledecu rec:")
        inp = input(">>>>")
        if int(inp) == 1:
            unos = input("Broj stranice:\n>>>>")
        else:
            break



def pretrazivanje_reci_i_prikaz():
    userInput = 1
    petlja = True
    n = 5
    while petlja:
        print("1 - Pretrazi rec: ")
        print("2 - Promenite broj stranica koje ce biti prikazane odjednom (trenutno %d)" % n)
        print("0 - Exit")
        userInput = input(">>>>>>>>")
        if int(userInput) == 1:
            querry = input("Unesite rec za pretrazivanje: ")

            ret_querry = upit.parsiraj_upit(querry)
            doc_list = upit.upitaj(trie, ret_querry[1], ret_querry[2], ret_querry[0], lista_dokumenata)

            #print(doc_list)
            print(doc_list.nmb_of_element())
            if doc_list.nmb_of_element() != 0:
                quick_sort(doc_list, 0, doc_list.nmb_of_element() - 1, graph, vertices)
                print("---------------------------------------------------------------")
                print("~~~~~~~~Trazena rec se pojavljuje u sledecim stranicama~~~~~~~~")
                prikaz_rezultata(n,doc_list)
                print("---------------------------------------------------------------")
            else:
                print("~~~~~~~~Trazena rec se ne pojavljuje ni u jednoj stranici izabranog direktorijuma~~~~~~~~")

        elif int(userInput) == 0:
            petlja = False
        elif int(userInput) == 2:
            n = promena_n()

        else:
            print("Nepoznata komanda")


if __name__ == "__main__":
    parser = Parser()
    graph = Graph(True)
    trie = Tree()
    root = trie.root
    lista_dokumenata = []
    vertices = {}
    korenski_dir = izaberi_direktorijum()

    print("Loading graph and trie....")

    napravi_cvorove(korenski_dir, graph, vertices)
    napravi_veze_i_drvo(korenski_dir, graph, vertices, parser, trie, lista_dokumenata)
    pretrazivanje_reci_i_prikaz()
