class Graph:
    def __init__(self, V): 
        self.vertices = [Vertex() for i in range(V)]

    def addEdges(self, v, E):
        self.vertices[v].edges.extend(E)
    
    def makeNumbers(self,V):
        for i in range(V): 
            self.vertices[i].number = i

class Vertex:
    def __init__(self):
        self.visited = False
        self.process = 0
        self.edges = []
        self.number = None

# wierzcholki usuwamy w kolejnosci przetworzenia dla DFS
# dziala bo jak jakis wierzcholek jest przetworzony to nie mozna z niego isc do innego -> mozna usunac

def delVertices(G: Graph):
    def dfs(G: Graph):
        def dfsVisit(u: Vertex):
            nonlocal G, time
            
            u.visited = True
            u.entry = time
            
            for v in u.edges:
                if not G.vertices[v].visited:
                    G.vertices[v].parent = u
                    dfsVisit(G.vertices[v])

            time += 1
            u.process = time
            
        time = 0
        for v in G.vertices:
            v.visited = False
            v.parent = None
        
        for v in G.vertices:
            if not v.visited:
                dfsVisit(v)
    
    dfs(G)
    G.vertices = sorted(G.vertices, key = lambda x: x.process)
    
    return([x.number for x in G.vertices])


H = Graph(8)
H.addEdges(0, [1,2])        #
H.addEdges(1, [0,2])        #   0----2------3------5
H.addEdges(2, [0,1,3])      #   |  /        |      |
H.addEdges(3, [2,4,5])      #   | /         |      |
H.addEdges(4, [3,6])        #   1           4 -----6----7
H.addEdges(5, [3,6])        #
H.addEdges(6, [4,5,7])      #
H.addEdges(7, [6])          #
H.makeNumbers(8)
print(delVertices(H))