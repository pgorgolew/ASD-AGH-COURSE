from queue import PriorityQueue, deque
# priorityQue robi minHeapa -> get daje najmniejeszy 
# O((V+E)*log(V)) -> dla listy sasiedztwa
def DijkstraNeighbours(G,v): #musza byc dodatnie wartosci krawedzi 
    n = len(G)
    d = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    done = [False for _ in range(n)]
    q = PriorityQueue()
    d[v] = 0
    q.put((d[v],v))
    while not q.empty():
        x, w = q.get()
        if done[w]: continue #bo dany wierzcholek moze byc pare razy w q

        for i in range(len(G[w])):
            t, road = G[w][i]
            if done[t] == False and x+road < d[t]:
                d[t] = x+road
                prev[t] = w
                q.put((d[t], t))

        done[w] = True
    
    for i in range(n):
        print(f"{createPath(prev,v,i)} -> {d[i]}")

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
    
    # for i in range(n):
    #     print(f"{createPath(prev,v,i)} -> {d[i]}")

def createPath(prev,s,t):
    #sciezka od s do t
    res = []
    if t == None: return res

    res = createPath(prev,s,prev[t])
    res.append(t)

    return res


G=[
    [0,4,3,0,0,0],
    [4,0,1,2,0,0],
    [3,1,0,4,3,0],
    [0,2,4,0,2,1],
    [0,0,3,2,0,6],
    [0,0,0,1,6,0]
]

H=[
    [(1,4),(2,3)],
    [(0,4),(2,1),(3,2)],
    [(0,3),(1,1),(3,4),(4,3)],
    [(1,2),(2,4),(4,2),(5,1)],
    [(2,3),(3,2),(5,6)],
    [(3,1),(4,6)]
]

from random import randint
import time

n = 1000
rr = (1, n)
G = [[0 if i == j else randint(rr[0], rr[1]) for i in range(n)] for j in range(n)]

start_time = time.time()
DijkstraMatrix(G,0)
print("--- %s seconds ---" % (time.time() - start_time))
