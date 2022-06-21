from collections import Queue
# Vertex is a number between 0 and V-1
# egdes is a list of neighbours (numbers beetwen 0 and V-1) 
class Graph:
    def __init__(self, V): 
        self.vertices = [Vertex() for i in range(V)]

    def addEdges(self, v, E):
        self.vertices[v].edges.extend(E)


class Vertex:
    def __init__(self):
        self.visited = False
        self.entry = 0
        self.process = 0
        self.edges = []
        self.parent = None
        self.d = 0

def dfs(G: Graph):
    def dfsVisit(u: Vertex):
        nonlocal G, time
        
        time += 1
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


def bfs(G: Graph, s: Vertex):
    queue = Queue()
    for v in G.vertices:
        v.visited = False
    
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


