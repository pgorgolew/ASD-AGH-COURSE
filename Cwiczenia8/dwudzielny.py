from queue import Queue

class Graph:
    def __init__(self, V): 
        self.vertices = [Vertex() for i in range(V)]

    def addEdges(self, v, E):
        self.vertices[v].edges.extend(E)

class Vertex:
    def __init__(self):
        self.visited = False
        self.edges = []
        self.d = 0
    
def bfs(G: Graph, s: Vertex):
    queue = Queue()
    
    s.d = 0
    s.visited = True
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        for v in u.edges:
            if not G.vertices[v].visited:
                G.vertices[v].visited = True
                G.vertices[v].d = u.d + 1
                queue.put(G.vertices[v])


# Jezeli po wykonaniu BFS, kazdy wierzcholek o odleglosci parzystej (nieparzystej)
# bedzie mial sasiadow o odleglosci nieparzystej (parzystej) to graf jest dwudzielny
def dwudzielny(G: Graph):
    if G.vertices == []: return False

    for v in G.vertices:
        v.visited = False
        
    # na wypadek gdyby graf nie byl spojny
    for v in G.vertices:
        if not v.visited:
            bfs(G, v) 

    for v in G.vertices:
        tmp = v.d
        for u in v.edges:
            if (tmp - G.vertices[u].d) % 2 == 0: #jezeli mieli taka sama parzystosc
                return False
    
    return True

H = Graph(8)
H.addEdges(0, [1,2])        #
H.addEdges(1, [0,2])        #   0----2------3------5
H.addEdges(2, [0,1,3])      #   |  /        |      |
H.addEdges(3, [2,4,5])      #   | /         |      |
H.addEdges(4, [3,6])        #   1           4 -----6----7
H.addEdges(5, [3,6])        #
H.addEdges(6, [4,5,7])      #
H.addEdges(7, [6])          #
print(dwudzielny(H))
