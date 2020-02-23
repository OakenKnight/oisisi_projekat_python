# Search Engine

U okviru projektnog zadatka implementirano je pretraživanje tekstualnih dokumenata (engl. search engine).
Program prilikom pokretanja obilazi stablo direktorijuma u datotečkom sistemu počevši
od datog korena, da parsira tekstualne datoteke u njima i da izgradi strukture podataka potrebne
za efikasno pretraživanje. Nakon toga, program omogućuje korisniku da unosi tekstualne upite
koji se sastoje od jedne ili više reči razdvojenih razmakom, pretražuje dokumente i korisniku ispisuje rangirane rezultate pretrage u vidu
putanja do dokumenata.

## Implementirane funkcionalosti

1.1 Parsiranje HTML dokumenata

Korisniku je omogućen izbor korenskog direktorijuma u okviru kojeg želi da pretražuje
dokumente. Dokumenti se pretražuju u zadatom direktorijumu kao i svim poddirektorijumima.


1.2 Unos upita za pretragu

Korisniku je omogućen unos upita koji može da se sastoji od jedne reči, više reči
razdvojenih razmakom ili kombinaciju reči sa logičkim operatorom.

Ukoliko se u upitu nalazi bar jedan od logičkih operatora ("and", "not", "or") onda je potrebno da se on nalazi u sredini (primer upita: python and/or/not java)

"Not" je implementiran takođe i kao unarni operator (primer upita: not python)

Ukoliko je upit unesen u nizu reči bez logičkih operatora, smatraće se da je "or" između reči (primer upita: python programming language...)


1.3. Pretraga dokumenata

Algoritam pretrage obilaskom strukture podataka (Tree) izdvoji sve HTML dokumente koji odgovaraju unetom upitu.

1.4 Rangirana pretraga

Implementirano je rangiranje rezultujućih stranica pretrage tako da na rang stranice utiče:

• broj pojavljivanja traženih reči na njoj,

• broj linkova iz drugih stranica na pronađenu stranicu

• broj traženih reči u stranicama koje sadrže link na traženu stranicu.


Ukoliko korisnik unosi upit sastavljen od više reči, rangiranje stranica po svakoj pojedinačnoj reči
utiče na sveukupno rangiranje određene stranice.

1.5 Prikaz rezultata pretrage

Rezultati upita su putanje do HTML stranica (iz test-skup) sortirane po izračunatom rangu.

1.6 Paginacija rezultata

Broj stranica koje se u jednom trenutku prikazuju može se dinamički promeniti od strane korisnika.




## Korišćene strukture podataka

Prilikom implementacije, potrebno je koristiti sledeće strukture podataka:

• HTML stranice test skupa podataka potrebno je organizovati u obliku usmerenog grafa
(Graph).

• Sve reči svih HTML stranica iz test skupa podataka potrebno je čuvati u trie stablu kako bi se omogućila efikasna pretraga (Tree).

• Rezultat pretrage jedne ili više reči treba da bude skup HTML stranica (Set - Lista_bez_duplikata).




## Uputstvo za upotrebu
Da bi program funkcionisao potrebno je da se test podaci ubace u folder test-skup.

Prilikom izbora korenskog direktorijuma omogućena su dva načina izbora.
1. Unos relativne adrese u odnosu na test-skup
2. Izbor jednog od ponuđenih direktorijuma



## Kreatori
[Radovan Župunski](https://www.facebook.com/radovan.zupunski)

[Aleksandar Ignjatijević](https://www.facebook.com/aleksandar.ignjatijevic19)
