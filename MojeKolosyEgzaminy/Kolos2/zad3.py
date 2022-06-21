from zad3testy import runtests
#f(i,j) - minimalna liczba zatrzyman potrzebna by dotrzec do i majac w zapasie
#         y jednostek paliwa (juz po zabraniu oleju M[i])

# f(i,y) = 1 + min_{k=1…(i-1)} { f(i-k,max{y+k-a[y],0}) }
# Rozwiązaniem jest min(f(n-1,0..n))

#zlozonosc m^2*n
#Funkcja zwraca ilosc zatrzyman
def plan(T):
    def olej(x,y,i):
        nonlocal n,m,used,T,M
        if used[y][x]: return

        M[i] += T[y][x]
        used[y][x] = True

        if y+1 < n and  T[y+1][x] != 0: olej(x,y+1,i)
        if x+1 < n and  T[y][x+1] != 0: olej(x+1,y,i)
        if y-1 > 0 and  T[y-1][x] != 0: olej(x,y-1,i)
        if x-1 > 0 and  T[y][x-1] != 0: olej(x-1,y,i)



    n = len(T)
    m = len(T[0])

    M = [0] * m

    used = [[False]*m for _ in range(n)]
    for i in range(m):
        if T[0][i] != 0 and not used[0][i]: 
            olej(i,0,i)
    
    s = sum(M)
    F = [[float("inf")]*(s+1) for _ in range(m)]

    F[0][M[0]] = 0 #warunek początkowy, na indeksie zero mamy olej A[0]

    for i in range(1,m):
        for j in range(s):
            for k in range(0,i):
                oil = j-M[i]+(i-k)
                if oil < (i-k): continue #bo nie mozna zrobic jechac majac za malo paliwa
                if oil > s or oil < 0: continue
                F[i][j] = min(F[i][j], F[k][oil]+1)

    x=0
    res = float("inf")
    for i in range(s+1):
        if F[m-1][i] < res: x,res = i, F[m-1][i]

        
    return res



    


runtests(plan)
