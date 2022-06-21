#f(i,j) - minimalna liczba skokow potrzebna by dotrzec do i majac w zapasie
#         y jednostek energii (juz po zjedzneiu przekaski A[i])
# f(i,y) = 1 + min_{k=1…(i-1)} { f(i-k,max{y+k-a[y],0}) }
# Rozwiązaniem jest min(f(n-1,0..n))

def zaba(A):
    n = len(A)
    s = sum(A)
    F = [[float("inf")]*(s+1) for _ in range(n)]

    F[0][A[0]] = 0 #warunek początkowy, na indeksie zero mamy energie A[0]

    for i in range(1,n):
        for j in range(s):
            for k in range(0,i):
                Energy = j-A[i]+(i-k)
                if Energy < (i-k): continue #bo nie mozna zrobic skoku majac za malo energi
                if Energy > s or Energy < 0: continue
                F[i][j] = min(F[i][j], F[k][Energy]+1)

    res = min(F[n-1][x] for x in range(s+1))
    return res

A = [1,7,1,1,1,2,0]
print(zaba(A))