# daje najmnijeszy path kazdej pary
#None w G oznacza brak krawedzi
def FloydWarshall(G): # O(V^3)
    n = len(G)
    D = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0: #jezeli istnieje krawedz
                D[i][j] = G[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] == 0:
                    if D[i][k] == 1 and D[k][j] == 1: D[i][j] = 1
    
    return D

G = [
    [0,0,0,1],
    [0,0, 1, 0],
    [0, 1, 0, 0],
    [1,0,0, 0]
]

d = FloydWarshall(G)
for i in d:
    print(i)