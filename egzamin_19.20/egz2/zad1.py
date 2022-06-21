from zad1testy import runtests
# f(i,j) - minimalna liczba skokow aby dotrzec do pola i z energia rowna j
def zbigniew( A ):
    s = sum(A)
    n = len(A)
    F = [[float("inf") for _ in range(s+1)] for _ in range(n)]
    
    F[0][A[0]] = 0
    for m in range(n):
        for e in range(1,s+1): #bo nie ma sensu rozwazac jak mamy 0 energii
            if F[m][e] == float("inf"): continue
            for x in range(1,e+1):
                if m+x >= n: break
                F[m+x][e-x+A[m+x]] = min(F[m+x][e-x+A[m+x]], F[m][e]+1)

    res = min(F[n-1][x] for x in range(s)) 
    return res if res < float("inf") else -1
       

runtests( zbigniew ) 
