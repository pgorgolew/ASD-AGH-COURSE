from zad3testy import runtests
from zad3EK    import edmonds_karp

# 1) Tworzymy tablice dystansów pomiedzy kazdymi wierzcholkami (V^3 bo Floyd-Warshall)
# 2) Tworzymy wszystkie kombinacje wierzcholkow spelniajacych warunki zadania (V^2)
# 3) Rekurencyjnie sprawdzamy ile najwiecej par mozemy wybrac

# zlozonosc czasowa O(V^3), pamieciowa O(V^2)
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

    return D

def BlueAndGreen(T, K, D):
    def findbest(p, used, i=0, last = 0, res=0):
        nonlocal best
        if i >= len(p):
            best = max(best, res)
            return

        if used[i]:
            findbest(p,used,i+1,last,res)
        else:
            for j in range(last, len(p)):
                if p[j][0] > i:
                    last = j+1 
                    break
                elif p[j][0] < i: continue

                if not used[p[j][1]]:
                    used[p[j][1]] = True
                    findbest(p,used,i+1,j+1,res+1)
                    used[p[j][0]] = False
            
            findbest(p, used, i+1, last, res)
                
    dist = FloydWarshall(T) # 1)
    n = len(T)
    p = []
    used = [False]*n
    for i in range(n-1): # 2)
        for j in range(i+1,n):
            if dist[i][j] >= D and K[i] != K[j]:
                p.append((i,j))

    used = [False]*n
    best = 0
    findbest(p,used) # 3)

    return best

runtests( BlueAndGreen ) 