def Mosty(G): #mosty dla reprezentacji macierzowej grafu
    def DFS(G,u,n):
        nonlocal d,parent,visited,low
        
        for i in range(n):
            if not visited[i] and G[u][i] == 1:
                parent[i] = u
                d[i] = d[u] + 1
                low[i] = d[i]
                visited[i] = True
                DFS(G,i,n)
            elif parent[u] != i and parent[u] != None and G[u][i] == 1:
                low[u] = min(low[u], d[i])
        
        if parent[u]: 
            low[parent[u]] = min(low[parent[u]], low[u])
                
    
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    d = [0]*n
    low = [None]*n

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            low[i] = d[i]
            DFS(G,i,n)
    
    res = []
    for i in range(n):
        if low[i] == d[i] and parent[i] != None:
            res.append((i,parent[i]))
    
    return res

G=[
    [0,1,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [1,0,0,0,0,0,0],
    [0,0,0,0,0,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0]
    ]

print(Mosty(G))