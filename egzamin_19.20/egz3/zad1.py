from zad1testy import runtests
def DFS(G,start): #Graf jako macierz sasiedztwa
    def DFSVisit(G,v):
        nonlocal visited, q, parent
        nonlocal maxi

        visited[v] = True
        for vert in G[v]:
            if not visited[vert]:
                parent[vert]=v
                q+=1

                if q > maxi[0]: maxi = (q,vert)

                DFSVisit(G,vert)
                q-=1

    # max1/2 = (dlugosc, ostatni wierzcholek)
    maxi= (0,0)
    n=len(G)
    visited = [False]*n
    parent = [None]*n
    q=0
    #graf spojny acykliczny neiskierowany wiec od liscia dojdziemy wszedzie
    #jedno wywolanie sprawdzi kazdy wierzcholek
    DFSVisit(G,start)

    return maxi, parent

def best_root( L ):
    n = len(L)
    #znajdz jakikolwiek lisc
    start = 0
    for i in range(n):
        if len(L[i])==1: 
            start=i
            break

    (lenght, end), parent = DFS(L,start)
    mid = lenght//2

    while lenght > mid:
        lenght-=1
        end=parent[end]
    
    return end



runtests( best_root ) 
