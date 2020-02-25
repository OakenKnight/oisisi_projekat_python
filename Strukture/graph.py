class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    # provera da li postoji trazeni cvor
    def _validate_vertex(self, v):
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    #da li je usmereni graf
    def is_directed(self):
        return self._incoming is not self._outgoing

    # broj ulaznih cvorova
    def count_of_incoming(self, v):
        self._validate_vertex(v)
        return len(self._incoming[v])

    #vraca vezu izmedju dva cvora
    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)

    # vraca ulazne i izlazne cvorove
    def get_in_out(self, v):
        self._validate_vertex(v)
        return self._incoming[v], self._outgoing

    # dodaje cvor
    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    # dodaje vezu od do
    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')

        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, x):
            """Do not call constructor directly.
                Use Graph's insert_vertex(x).
                """
            self._element = x

        def element(self):
            """Return element associated with this vertex."""
            return self._element

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

    class Edge:
        __slots__ = '_origin', '_destination', '_elements'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._elements = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            if not isinstance(v, Graph, Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin
            raise ValueError('v not incident to edge')

        def element(self):
            return self._elements

        def __hash__(self):
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2}))'.format(self._origin, self._destination, self._elements)
