from collections import deque

def find4Cycles(G):
    def bfs(G,v,n):
        nonlocal verticlesDone
        nonlocal res

        ones = []
        visited = [False] * n
        parent = [None] * n
        distance = [-1] * n
        distance[v] = 0

        Q = deque()
        Q.append(v)
        visited[v] = True
        while Q:
            z = Q.popleft()
            if distance[z] == 2: break
            for u in range(n):
                if not visited[u] and G[z][u] == 1:
                    visited[u] = True
                    parent[u] = z
                    distance[u] = distance[z] + 1
                    Q.append(u)
                    if distance[u] == 1: ones.append(u)
        
        for u in range(n):
            if distance[u] == 2:
                for z in range(n):
                    if G[u][z] == 1 and z != parent[u] and distance[z] == 1:
                        t = sorted([v,z,u,parent[u]])
                        if t in verticlesDone: continue
                        res.append((v,z,u,parent[u]))
                        verticlesDone.append(t)
        
        k = len(ones)
        for i in range(k-2):
            for j in range(i+1,k-1):
                for z in range(j+1,k):
                    t = sorted([v,ones[z],ones[i],ones[j]])
                    if t in verticlesDone: continue

                    if G[ones[i]][ones[j]] == 1 and G[ones[i]][ones[z]] == 1:
                        res.append((v,ones[z],ones[i],ones[j]))
                    
                    if G[ones[j]][ones[z]] == 1 and G[ones[j]][ones[i]] == 1:
                        res.append((v,ones[z],ones[j],ones[i]))
                    
                    if G[ones[z]][ones[i]] == 1 and G[ones[z]][ones[j]] == 1:
                        res.append((v,ones[i],ones[z],ones[j]))
                    
                    verticlesDone.append(t)

        return res

    n = len(G)
    res = []
    verticlesDone = []
    for v in range(n):
        bfs(G,v,n)

    return res

G = [
    [0,1,1,1,1],
    [1,0,1,1,1],
    [1,1,0,1,1],
    [1,1,1,0,1],
    [1,1,1,1,0]
    ]

res = find4Cycles(G)
for t in res:
    print(t)