import time

import upit
from parser import Parser
from graph import Graph
from tree import Tree
from treeNode import TreeNode
import os
from sort import *

i = 10
l = 0


def napravi_cvorove(file_path, graph, vertices, lista_dokumenata, mapa):  # pravim mapu i listu
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = os.path.join(file_path, fajl)

        if os.path.isdir(putanja):
            napravi_cvorove(putanja, graph, vertices, lista_dokumenata, mapa)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            vertices[putanja] = graph.insert_vertex(putanja)
            mapa[putanja] = 0  # pravim mapu
            lista_dokumenata.append(putanja)


def napravi_veze_i_drvo(file_path, graph, vertices, parser, trie):
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = os.path.join(file_path, fajl)

        if os.path.isdir(putanja):
            napravi_veze_i_drvo(putanja, graph, vertices, parser, trie)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            parseHtml(file_path, trie, parser, fajl, vertices, graph, mapa)


def parseHtml(file_path, trie, parser, fajl, vertices, graph, mapa):
    global l
    l = l + 1
    putanja1 = os.path.join(file_path, fajl)
    ret = parser.parse(putanja1)
    links = ret[0]
    napravi_veze(vertices[putanja1], links, graph, vertices)
    words = ret[1]
    for word in words:
        trie.add_word(word.lower(), putanja1, mapa)

def win_or_lin():
    if "/" in os.path.abspath("test-skup"):
        slash = "/"
    elif "\\" in os.path.abspath("test-skup"):
        slash = "\\"
    else:
        print("Nesto ne valja sa adresom!!!")
    return slash

def napravi_veze(vert, edg, graph, vertices):
    global i
    for v in edg:
        if v.endswith("html") or v.endswith("htm"):
            slash = win_or_lin()
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


def proveri_postojanje(trie, word):
    if trie.does_word_exist(word)[1] is None:
        print("Ne postoji ta rec!")
    else:
        ret = trie.does_word_exist(word.lower())
        print(ret[2].keys())


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
    slash = win_or_lin()
    if int(unos) == 1:
        petlja = True
        while petlja:
            print('Unesite adresu(npr. test-skup'+slash+'...'+slash+'...'+slash+'...):')
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
        slash = win_or_lin()
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
        try:
            uneseno = int(unos)
        except ValueError:
            print("Nije unesen broj!")
            continue
        if uneseno < 1:
            print("Nemoguce je prikazati manje od 1 stranice!!!")
        else:
            return uneseno


def ispis(doc, i, rang):
    (inc, outg) = graph.get_in_out(vertices[doc])
    print(i, ".", doc)
    print("\t\t-Rang stranice:", rang)
    # print("\t\t-Broj stranica koje pokazuju na ovu stranicu:", len(inc))
    # print("\t\t-Broj stranica na koje pokazuje ova stranica:", len(outg))


def prikaz_rezultata(n, doc_list, rangovi):
    petlja = True
    unos = 1
    broj_stranica = int(doc_list.nmb_of_element() / n + 0.999)
    # print(broj_stranica)
    # da li ovde treba da se unese zastita??
    while petlja:
        # print(doc_list)
        for i in range((int(unos) - 1) * n, int(unos) * n):
            if i < doc_list.nmb_of_element():
                ispis(doc_list[i], i + 1, rangovi[doc_list[i]])
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
        try:
            uneseno = int(inp)
        except ValueError:
            print("Nije dobar unos! Unesite broj!")
            continue
        if uneseno == 1:
            unos = input("Broj stranice:\n>>>>")
        elif uneseno == 2:
            break
        else:
            print("Nepoznata komanda!!!")


def pretrazivanje_reci_i_prikaz():
    userInput = 1
    petlja = True
    n = 5
    while petlja:
        print("1 - Pretrazi rec: ")
        print("2 - Promenite broj stranica koje ce biti prikazane odjednom (trenutno %d)" % n)
        print("0 - Exit")
        userInput = input(">>>>>>>>")

        try:
            user_inp = int(userInput)
        except ValueError:
            print("Nije unesen broj! Unesite opet!")
            continue

        if user_inp == 1:
            querry = input("Unesite rec za pretrazivanje: ")

            ret_querry = upit.parse(querry)
            ret = upit.upitaj(trie, ret_querry[1], ret_querry[2], ret_querry[0], lista_dokumenata)
            doc_list = ret[0]
            ponavljanja = ret[1]
            # print(ponavljanja.keys())
            # print(doc_list.nmb_of_element())

            if doc_list.nmb_of_element() != 0:
                start = time.time()
                rang = rang_svih(ponavljanja,vertices,graph,doc_list)
                quick_sort(doc_list, 0, doc_list.nmb_of_element() - 1, rang)
                print(time.time()-start)
                print("---------------------------------------------------------------")
                print("~~~~~~~~Trazena rec se pojavljuje u sledecim stranicama~~~~~~~~")
                prikaz_rezultata(n, doc_list, rang)
                print("---------------------------------------------------------------")
            else:
                print("~~~~~~~~Trazena rec se ne pojavljuje ni u jednoj stranici izabranog direktorijuma~~~~~~~~")

        elif user_inp == 0:
            petlja = False
        elif user_inp == 2:
            n = promena_n()

        else:
            print("Nepoznata komanda")


if __name__ == "__main__":
    parser = Parser()
    graph = Graph(True)

    lista_dokumenata = []
    vertices = {}
    mapa = {}
    korenski_dir = izaberi_direktorijum()

    print("Loading graph and trie....")

    napravi_cvorove(korenski_dir, graph, vertices, lista_dokumenata, mapa)

    trie = Tree(mapa)
    root = trie.root

    napravi_veze_i_drvo(korenski_dir, graph, vertices, parser, trie)
    pretrazivanje_reci_i_prikaz()
