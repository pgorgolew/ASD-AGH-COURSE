from queue import deque

def Kapitan(G,T):
    if G[0][0] <= T: return False
    q = deque()
    n = len(G)
    q.append((0,0))

    while q:
        x, y = q.popleft()
        G[x][y] = 0 #zeby sie nie odpalalo pozniej na tym samym wierzcholku

        if x == y == n-1: return True
        if x > 0 and G[x-1][y] > T:
            q.append((x-1,y))
        
        if x < n-1 and G[x+1][y] > T:
             q.append((x+1,y))

        if y > 0 and G[x][y-1] > T:
            q.append((x,y-1))
        
        if y < n-1 and G[x][y+1] > T:
             q.append((x,y+1))

    return False
    
G =[
    [4,1,5,2,1,1],
    [5,1,1,5,5,1],
    [5,5,4,8,5,1],
    [1,1,1,2,5,1],
    [1,5,5,5,5,5],
    [1,1,1,1,1,7]
]

print(Kapitan(G,3))