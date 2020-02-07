from parser import Parser
from graph import Graph
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



if __name__ == "__main__":
    parser = Parser()
    graph = Graph(True)
    vertices = {}
    ucitaj_fajlove("/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html", graph, vertices)
    for element in graph.vertices():
        edg = parser.parse(str(element))
        napravi_veze(element, edg[0], graph, vertices)

    print(graph.get_edge(vertices["/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/genindex-K.html"], vertices["/home/radovan/Documents/python/Projekat_OISISI/python-2.7.7-docs-html/library/curses.html"]))

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
