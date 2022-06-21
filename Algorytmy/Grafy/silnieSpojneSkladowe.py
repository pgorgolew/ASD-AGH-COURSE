def silnieSpojne(G):
    def DFS(G,i,n):
        nonlocal time, times, visited

        visited[i] = True
        for u in range(n):
            if G[i][u] == 1 and not visited[u]:
                visited[u]=True
                DFS(G,u,n)
        
        time += 1
        times[i] = time
    
    def DFS2(G,u,n,k):
        nonlocal visited, times, res

        visited[u] = False
        res[k].append(u)
        times[u] = 0

        for i in range(n):
            if visited[i] and G[u][i] == 1:
                DFS2(G,i,n,k)

        return len(res[k])
    def reverseEdges(G):
        n = len(G)
        H = [[] for _ in range(n)]
        for v in range(n):
            for u in range(n):
                if G[v][u] == 1:
                    H[u].append(1)
                else:
                    H[u].append(0)
        return H

    n = len(G)
    time = 0
    visited = [False]*n
    times = [0]*n
    for i in range(n):
        if not visited[i]:
            DFS(G,i,n)
    
    G = reverseEdges(G)

    res = []
    amount = n
    while amount > 0:
        tmp = max(times)
        for i in range(n):
            if times[i] == tmp:
                res.append([])
                amount -= DFS2(G,i,n,len(res)-1)
    
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

print(silnieSpojne(G))
    