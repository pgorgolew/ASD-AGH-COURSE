from zad3testy import runtests

def Sort(G): #Graf jako macierz
    def DFSVisit(G,n,v):
        nonlocal visited, res

        visited[v] = True
        for i in range(n):
            if not visited[i] and G[v][i]==1:
                DFSVisit(G,n,i)
        
        res.append(v)

    n=len(G)
    visited = [False]*n
    res = []
    for v in range(n):
        if not visited[v]:
            DFSVisit(G,n,v)
    
    res.reverse()

    return res

def tasks(T):
    return Sort(T)



runtests( tasks )
