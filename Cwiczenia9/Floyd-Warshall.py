# daje najmnijeszy path kazdej pary
#None w G oznacza brak krawedzi
def FloydWarshall(G): # O(V^3)
    n = len(G)
    D = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != None: #jezeli istnieje krawedz
                D[i][j] = G[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    
    return D

G = [
    [0,None,-2,None],
    [4,0, 3, None],
    [None, None, 0, 2],
    [None,-1,None, 0]
]

d = FloydWarshall(G)
for i in d:
    print(i)