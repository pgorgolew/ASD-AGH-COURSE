def DijkstraMatrix(G,v): # O(V^2)
    def findMinimumVer(n,d,done):
        p = float("inf")
        i = None
        for v in range(n):
            if not done[v]:
                if d[v] < p:
                    i = v
                    p = d[v]
        
        return i
    
    n = len(G)
    d = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    done = [False for _ in range(n)]
    d[v] = 0
    while v != None:
        for i in range(n):
            if G[v][i] != 0 and not done[i] and d[v]+G[v][i] < d[i]:
                d[i] = d[v]+G[v][i]
                prev[i] = v

        done[v] = True

        v = findMinimumVer(n,d,done)