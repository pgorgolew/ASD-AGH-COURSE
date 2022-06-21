def find4Cycle(G): #N^3

    n = len(G)
    if n < 4: return False
    
    F = [[]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0: continue
            for k in range(n):
                if G[j][k]==0: continue 
                F[i][k].append(j)
                for z in F[k][i]:
                    if z != j:
                        return True #i->j->k->z
    
def find4CyclesN4(G): #N^4 :(
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0: continue
            for z in range(n):
                if G[j][z] == 0 or i == z: continue
                for k in range(n):
                    if G[z][k] == 0 or G[k][i] == 0 or k == j: continue
                    return True
    
    return False

G = [
    [0,1,0,1,1],
    [1,0,1,1,1],
    [0,1,0,1,0],
    [1,1,1,0,1],
    [1,1,0,1,0]
    ]

res = find4Cycle(G)
print(res)   