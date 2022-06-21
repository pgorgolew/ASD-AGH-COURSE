#Daje path taki jak Dijsktra ale mozna ujemne

def BellmanFord(G,v): # O(n^3)
    n=len(G)
    D = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]

    D[v] = 0

    for i in range(n-1):
        for j in range(n):
            for z in range(n):
                if G[j][z] != 0:
                    if D[j] + G[j][z] < D[z]:
                        D[z] = D[j] + G[j][z]
                        prev[z] = j
    
    for j in range(n): #spr czy jest cykl ujemny
        for z in range(n):
            if G[j][z] != 0:
                if D[z] > D[j] + G[j][z]: #means mamy cykl o ujemnej sumie
                    print("CYKL O UJEMNEJ SUMIE")
                    return
    
    for i in range(n):
        print(f"{createPath(prev,v,i)} -> {D[i]}")

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

BellmanFord(G,0)