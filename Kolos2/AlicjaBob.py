from queue import PriorityQueue

def Alicja(G,x,y): #z x do y
    def bfs(k): #bfs ktory dodaje dystans jezeli jedzie ala czyli k parzyste
        nonlocal n,G,x,y

        visited = [False]*n
        q = PriorityQueue()
        parent = [None]*n

        q.put((x,0,k,None))

        while q:
            d,v,k,p = q.get()
            if visited[v] == True: continue
            parent[v] = p
            if v == y: return parent, d

            for i in range(n):
                if visited[i] == False and G[v][i] != 0:
                    if k % 2 == 1: #teraz jedzie Bob
                        q.put((d,i,k+1,v))
                    else: #teraz jedzie ALA
                        q.put((d+G[v][i], i, k+1, v)) 
                visited[v] = True
    
    def result(y, res=[]):
        nonlocal p2

        if p2[y] != None:
            result(p2[y])
        
        res.append(y)
        return res

    n = len(G)
    p1,d1 = bfs(0) #zaczyna ALA
    p2,d2 = bfs(1) #zaczyna BOB

    first = "BOB"
    if d1 < d2:
        d2,p2 = d1,p1
        first = "ALA"
    
    path = result(y)

    return path, first

            
G = [
    [0,4,8,0,0,0,0,0,0],
    [4,0,0,3,0,0,0,0,0],
    [8,0,0,6,0,0,0,0,0],
    [0,3,6,0,5,0,2,0,0],
    [0,0,0,5,0,20,0,1,0],
    [0,0,0,0,20,0,0,0,7],
    [0,0,0,2,0,0,0,7,0],
    [0,0,0,0,1,0,7,0,4],
    [0,0,0,0,0,7,0,4,0]
]

print(Alicja(G,0,5))


