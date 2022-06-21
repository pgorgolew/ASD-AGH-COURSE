from queue import deque

def func(G):
    q = deque()
    n = len(G)
    P=[[None for _ in range(n)] for _ in range(n)]
    q.append(((0,0), 1, (-1,-1)))

    while q:
        i, t, p = q.popleft()
        if t>1: 
            q.append((i,t-1,p))
            continue
        
        x,y = i
        P[x][y] = p
        if x > 0 and P[x-1][y] == None:
            q.append(((x-1,y), G[x-1][y], (x,y)))
        
        if x < n-1 and P[x+1][y] == None:
             q.append(((x+1,y), G[x+1][y], (x,y)))

        if y > 0 and P[x][y-1] == None:
            q.append(((x,y-1), G[x][y-1], (x,y)))
        
        if y < n-1 and P[x][y+1] == None:
             q.append(((x,y+1), G[x][y+1], (x,y)))

    p = (n-1,n-1)
    while p != (-1,-1):
        x,y = p
        print(f"({x},{y})", end=" ")
        p = P[x][y]
    

G =[
    [1,1,5,2,1,1],
    [5,1,1,5,5,1],
    [5,5,1,1,5,1],
    [1,1,1,2,5,1],
    [1,5,5,5,5,5],
    [1,1,1,1,1,1]
]

func(G)