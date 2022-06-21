class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


def make_set(x):
    return Node(x)


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(G): #graf listy sasiedztwa gdzie G[i] zawiera krotki (wierzcholek, waga krawedzi)
    n = len(G)
    result = [[] for _ in range(n)]
    edges = []
    vertices = []
    for i in range(n):
        vertices.append(make_set(i))
        for j in range(len(G[i])):
            edges.append((i,G[i][j][0],G[i][j][1]))
    
    edges = sorted(edges, key=lambda tup: tup[2])

    for (s,t,d) in edges:
        if find_set(vertices[s]) != find_set(vertices[t]):
            union(vertices[s],vertices[t])
            result[s].append((t,d))
            result[t].append((s,d))
    
    return result

H=[
    [(1,4),(2,3)],
    [(0,4),(2,1),(3,2)],
    [(0,3),(1,1),(3,4),(4,3)],
    [(1,2),(2,4),(4,2),(5,1)],
    [(2,3),(3,2),(5,6)],
    [(3,1),(4,6)]
]

r = Kruskal(H)
for row in r:
    print(row)