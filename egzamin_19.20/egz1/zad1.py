from zad1testy import runtests
# Algorytm wykonuje zmodyfikowaną dijsktre ktora rozroznia 3 stany wierzcholka
# zalezne od tego, jakim transportem ostatnio sie poruszal

# zlozonosc czasowa to dijsktra dla 3*n wieszchołkow
# O((3V)^2) = O(9V^2) = O(V^2)
def DijkstraMatrix(G,v,t): # O(V^2)
    def findMinimumVer(n,d,done):
        p = float("inf")
        i = None
        k = None
        for v in range(n):
            for z in range(3):
                if not done[v][z]:
                    if d[v][z] < p:
                        i = v
                        k = z
                        p = d[v][z]
            
        return i, k
    
    n = len(G)
    # d[v][i] - koszt dojscia do v gdzie ostatnim transpotem bylo i
    # d[v][0] - 1$, d[v][1] - 5$, d[v][2] - 8$ 
    d = [[float("inf"), float("inf"), float("inf")] for _ in range(n)]
    done = [[False,False,False] for _ in range(n)]
    d[v] = [0,0,0]
    costs = [1,5,8]
    k = 0
    while v != None and v != t:
        for i in range(n):
            p = G[v][i]
            if p == 0 or p == costs[k]: continue
            
            if p == 1 and d[i][0] > d[v][k] + p and not done[i][0]:
                d[i][0] = d[v][k] + p
            
            elif p == 5 and d[i][1] > d[v][k] + p and not done[i][1]:
                d[i][1] = d[v][k] + p
            
            elif p == 8 and d[i][2] > d[v][k] + p and not done[i][2]:
                d[i][2] = d[v][k] + p

        done[v][k] = True

        v, k = findMinimumVer(n,d,done)
    
    return d[v][k] if v != None else None

def islands(G, A, B):
    return DijkstraMatrix(G,A,B)
        

runtests( islands ) 
