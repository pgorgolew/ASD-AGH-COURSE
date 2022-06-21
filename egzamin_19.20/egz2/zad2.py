from zad2testy import runtests
from math import ceil, sqrt

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

def Kruskal(G): #graf listy sasiedztwa gdzie G[i] zawiera krotki (wierzcholek, waga krawedzi, ujemne badz dodatnie)
    n = len(G)
    result = [[] for _ in range(n)]
    edges = []
    vertices = []
    for i in range(n):
        vertices.append(make_set(i))
        for j in range(len(G[i])):
            edges.append((i,G[i][j][0],G[i][j][1], G[i][j][2]))
    
    edges = sorted(edges, key=lambda tup: tup[2])

    for (s,t,d,sign) in edges:
        if find_set(vertices[s]) != find_set(vertices[t]):
            union(vertices[s],vertices[t])
            result[s].append((t,d,sign))
            result[t].append((s,d,sign))
    
    return result

def highway(A):
    n=len(A)
    G=[]

    #budujemy liste krawedzi z dodatkowym pole na czas budowy autostrady
    for i in range(n-1):
        for j in range(i+1,n):
            G.append((i, j, ceil(sqrt((A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2 ))))
    
    best = float("inf")
    for edge in G:
        base = edge[2]
        H = [[] for _ in range(n)]
        m = 0 #szukamy najbardziej ujemnej liczby
        for e in G:
            tmp = e[2]-base
            h = 1
            if tmp < 0: h = -1
            H[e[0]].append((e[1], abs(tmp), h))
            H[e[1]].append((e[0], abs(tmp), h))

        mini = maxi = 0
        K = Kruskal(H)
        
        for i in range(n):
            for j in range(len(K[i])):
                mini = min(mini, K[i][j][1]*K[i][j][2])
                maxi = max(maxi, K[i][j][1]*K[i][j][2])
    
        best = min(best, maxi-mini)

    return best
runtests( highway ) 
