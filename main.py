import os
import time

from Parseri import upit
from Strukture.graph import Graph
from Parseri.parser import Parser
from Sortiranje.sort import *
from Strukture.tree import Tree

i = 1
l = 0


# formiraju se cvorovi grafa
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


# formiraju se veze izmedju cvorova grafa i stablo
def napravi_veze_i_drvo(file_path, graph, vertices, parser, trie):
    fajlovi = os.listdir(file_path)
    for fajl in fajlovi:
        putanja = os.path.join(file_path, fajl)

        if os.path.isdir(putanja):
            napravi_veze_i_drvo(putanja, graph, vertices, parser, trie)
        elif fajl.endswith("html") or fajl.endswith("htm"):
            parseHtml(file_path, trie, parser, fajl, vertices, graph, mapa)


# parsiranje svake html stranice i pozivanje funkcija za pravljenje veza i stabla
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


# funkcija za odredjivanje da li ce se parsirati po '/' ili '\'
def win_or_lin():
    if "/" in os.path.abspath("test-skup"):
        slash = "/"
    elif "\\" in os.path.abspath("test-skup"):
        slash = "\\"
    else:
        print("Nesto ne valja sa adresom!!!")
    return slash


# pravi veze izmedju html stranica
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
            i = i + 1


#
def proveri_postojanje(trie, word):
    if trie.does_word_exist(word)[1] is None:
        print("Ne postoji ta rec!")
    else:
        ret = trie.does_word_exist(word.lower())
        print(ret[2].keys())


# funkcija proverava da li je prosledjena putanja direktorijum
def postoji_direktorijum(file_path):
    if os.path.isdir(file_path):
        return True
    else:
        return False


# funkcija koja se poziva na pocetku programa da bi korisnik mogao da odabere da li zeli da bira ponudjene direktorijume
# ili zeli sam da unosi relativnu adresu u odnosu na 'test-skup' fajl
def rucno_unos_direktorijuma():
    while True:
        print("1 - Unos relativne adrese u odnosu na 'test-skup'")
        print("2 - Odabir jednog od ponudjenih direktorijuma iz 'test-skup' direktorijuma")
        unos = input(">>>>")
        try:
            test = int(unos)
        except ValueError:
            print("----Nije unesen broj! Molimo Vas pokusajte ponovo----")
            continue
        adresa = ""
        slash = win_or_lin()
        if int(unos) == 1:
            petlja = True
            while petlja:
                print('-Unesite adresu(npr. test-skup' + slash + '...' + slash + '...' + slash + '...):')
                adresa = input(">>>>")
                if "test-skup" in adresa:
                    if postoji_direktorijum(adresa):
                        petlja = False
                    else:
                        print("----Zeljena adresa ne postoji kao poddirektorijum 'test-skup' direktorijuma----")
                else:
                    adresa = os.path.join("test-skup", adresa)
                    if postoji_direktorijum(adresa):
                        petlja = False
                    else:
                        print("----Zeljena adresa ne postoji kao poddirektorijum 'test-skup' direktorijuma----")
                        print("----Proverite da li ste ispravno uneli adresu----")
            return True, adresa
        elif int(unos) == 2:
            return False, ""
        else:
            print("----Nepoznata komanda----")


# funkcija koja omogucava izbor direktorijuma ukuliko se korisnik odluci za tu opciju
# u suprotnom prosledjuje direktorijum koji je korisnik sam uneo
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
                print("----Trenutni direktorijum nema poddirektorijume----")
                print(
                    "-1 - Povratak u prethodni direktorijum\n 0 - Ostanak u trenutnom direktorijumu")
                unos = input(">>>>")
                try:
                    uneseno = int(unos)
                except ValueError:
                    print("----Nije unesen broj! Molimo Vas pokusajte ponovo----")
                    continue
                if uneseno == -1:
                    st = korenski_dir.split(slash)
                    duzina_poslednjeg = len(st[len(st) - 1]) + 1
                    korenski_dir = korenski_dir[: -duzina_poslednjeg]
                    continue
                elif uneseno == 0:
                    petlja = False
                    print("Izabrali ste direktorijum: ", str(korenski_dir))
                    continue
                else:
                    print("----Nepoznata komanda----")
            elif i != 1:
                print(
                    "-Izaberite broj direktorijuma:\n-1 - Povratak u prethodni direktorijum\n 0 - Ostanak u trenutnom direktorijumu")
                unos = input(">>>>")
                try:
                    uneseno = int(unos)
                except ValueError:
                    print("----Nije unesen broj! Molimo Vas pokusajte ponovo----")
                    continue

                if uneseno < i and uneseno > 0:
                    korenski_dir = os.path.join(str(korenski_dir), poddirektorijumi[int(unos) - 1])
                elif uneseno == -1:
                    st = korenski_dir.split(slash)
                    if len(st) == 1:
                        print("----Nalazite se u prvom direktorijumu!!!(Nema 'nadredjenih' direktorijuma)----")
                        continue
                    duzina_poslednjeg = len(st[len(st) - 1]) + 1
                    korenski_dir = korenski_dir[: -duzina_poslednjeg]
                    continue
                elif uneseno == 0:
                    print("Izabrali ste direktorijum: ", str(korenski_dir))
                    petlja = False
                else:
                    print("----Nepostojeca komanda----")
        return korenski_dir


# funkcija koja omogucava korisniku da promeni broj rezultata koji ce se prikazivati odjednom
def promena_n():
    while True:
        print("-Koliko stranica zelite da se prikaze odjednom(ceo broj 0<N<51):")
        unos = input(">>>>")
        try:
            uneseno = int(unos)
        except ValueError:
            print("----Nije unesen broj----")
            continue
        if uneseno < 1:
            print("----Nemoguce je prikazati manje od 1 stranice----")
        elif uneseno > 50:
            print("----Prevelik broj stranica(maksimum 50)----")
        else:
            return uneseno


# ispis jednog rezultata
def ispis(doc, i, rang, br_reci, reci_u_linkovima):
    (inc, outg) = graph.get_in_out(vertices[doc])
    print(i, ".", doc)
    print("\t\t-Rang stranice:", round(rang, 3))
    print("\t\t-Broj trazenih reci:", br_reci)
    print("\t\t-Broj linkova na ovu stranicu:", len(inc))
    print("\t\t-Broj trazenih reci u linkovima:", reci_u_linkovima)


# formatiran ispis svih rezultata razvrstan po stranicama uz mogucnost 'setanja' kroz stranice
def prikaz_rezultata(n, doc_list, rangovi, ponavljanja, br_reci_u_linkovima):
    petlja = True
    unos = 1
    broj_stranica = int(doc_list.nmb_of_element() / n + 0.99999)
    # da li ovde treba da se unese zastita??
    while petlja:
        # print(doc_list)
        for i in range((int(unos) - 1) * n, int(unos) * n):
            if i < doc_list.nmb_of_element():
                ispis(doc_list[i], i + 1, rangovi[doc_list[i]], ponavljanja[doc_list[i]],
                      br_reci_u_linkovima[doc_list[i]])
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
        print("2 - Nazad")
        print("0 - Izlaz")
        inp = input(">>>>")
        try:
            uneseno = int(inp)
        except ValueError:
            print("----Nije dobar unos! Unesite broj----")
            continue
        if uneseno == 1:
            while (True):
                unos = input("-Broj stranice:\n>>>>")
                try:
                    unos = int(unos)
                except ValueError:
                    print("----Nije dobar unos! Unesite ceo broj----")
                    continue
                if unos > broj_stranica or unos < 1:
                    if broj_stranica == 1:
                        print("-Za unetu pretragu postoji samo jedna stranica")
                    else:
                        print("-Izaberite stranicu iz opsega [1,%d]" % broj_stranica)
                else:
                    break
        elif uneseno == 2:
            return False
        elif uneseno == 0:
            return True
        else:
            print("----Nepoznata komanda----")


# funkcija koja omogucava unos trazenih reci, poziva funkcije za trazenje reci, rangiranje, sortiranje, ispis...
def pretrazivanje_reci_i_prikaz():
    userInput = 1
    petlja = True
    n = 5
    while petlja:
        print("1 - Pretrazi rec: ")
        print("2 - Promenite broj stranica koje ce biti prikazane odjednom (trenutno %d)" % n)
        print("0 - Izlaz")
        userInput = input(">>>>>>>>")

        try:
            user_inp = int(userInput)
        except ValueError:
            print("----Nije unesen broj! Unesite opet----")
            continue

        if user_inp == 1:
            querry = input("-Unesite rec za pretrazivanje: ")

            ret_querry = upit.parse(querry)
            ret = upit.upitaj(trie, ret_querry[1], ret_querry[2], ret_querry[0], lista_dokumenata)
            doc_list = ret[0]
            ponavljanja = ret[1]

            if doc_list is not None:
                if doc_list.nmb_of_element() == 0:
                    continue
                else:
                    start = time.time()
                    (rang, br_reci_u_linkovima) = rang_svih(ponavljanja, vertices, graph, doc_list)
                    quick_sort(doc_list, 0, doc_list.nmb_of_element() - 1, rang)
                    # print(time.time() - start)
                    print("---------------------------------------------------------------")
                    print("~~~~~~~~Trazena rec se pojavljuje u sledecim stranicama~~~~~~~~")
                    if prikaz_rezultata(n, doc_list, rang, ponavljanja, br_reci_u_linkovima):
                        break

                    print("---------------------------------------------------------------")

            elif doc_list is None:

                print("~~~~~~~~Trazeni unos se ne pojavljuje ni u jednoj stranici izabranog direktorijuma~~~~~~~~")

        elif user_inp == 0:
            petlja = False
        elif user_inp == 2:
            n = promena_n()

        else:
            print("----Nepoznata komanda----")


if __name__ == "__main__":
    parser = Parser()
    graph = Graph(True)

    lista_dokumenata = []
    vertices = {}
    mapa = {}
    korenski_dir = izaberi_direktorijum()

    print("Ucitavanje grafa i stabla....")

    napravi_cvorove(korenski_dir, graph, vertices, lista_dokumenata, mapa)

    trie = Tree(mapa)
    root = trie.root

    napravi_veze_i_drvo(korenski_dir, graph, vertices, parser, trie)
    pretrazivanje_reci_i_prikaz()
