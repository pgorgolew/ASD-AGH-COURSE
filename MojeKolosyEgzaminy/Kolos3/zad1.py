from zad1testy import runtests


# 1) tworzymy tablice dysansow
# 2) tworzymy tablice visted zawierajaca wszystkie mozliwe krotki (x1,y1)
# 3) rekurencyjnie staramy sie przejsc po "nowym" grafie od wierzcholka (x,y) do (y,x), tak
#    aby spelnic warunki zadania

#zlozonosc pamieciowa V^2, czasowa V^3 na pewno, zalezy od rekurencyjnego szukania
def FloydWarshall(G): # O(V^3)
    n = len(G)
    D = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0: #jezeli istnieje krawedz
                D[i][j] = G[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]

    for j in range(n):
        D[j][j] = 0

    return D

def keep_distance(M, x, y, d):
    def findWay():
        nonlocal D,M,stack,visited,d,x,y,f

        cx, cy = stack[-1]
        if cx == y and cy == x:
            f=True
            return

        for i in range(n):
            for j in range(n):
                if not visited[i][j] and D[i][j] >= d:
                    if i != cx and M[i][cx] == 0: continue #musi istniec krawedz
                    if j != cy and M[j][cy] == 0: continue #musi istniec krawedz
                    if cx == j and cy == i: continue #przejscie po tej samej krawedzi
                    stack.append((i,j))
                    visited[i][j] = True
                    findWay()
                    if f: return
                    stack.pop()
                    visited[i][j] = False

        return 
    
    D = FloydWarshall(M)
    n = len(M)

    stack = [(x,y)]
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    f=False
    findWay()

    if len(stack)<2: return None 

    return stack


runtests( keep_distance )