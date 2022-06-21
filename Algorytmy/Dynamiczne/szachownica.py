#mozemy poruszac sie tylko w prawo i w do, zatem jest tylko jedna droga do [n][0] i [0][n]
#nastepnie bedziemy sprawdzac, dla kazdej komórki, czy lepiej isc do niej od gory czy od lewej

def szachyMachy(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]
    F[0][0] = A[0][0]
    for i in range(1,n):
        F[0][i] = A[0][i] + F[0][i-1]
        F[i][0] = A[i][0] + F[i-1][0]

    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = min(F[i-1][j], F[i][j-1]) + A[i][j]
    
    T = trasa(F,A,n-1,n-1)
    T2 = trasa2(F,A,n)

    return(F[n-1][n-1], T2)

def trasa2(F,A,n):
    i = j = n-1
    T = [[" " for _ in range(n)] for _ in range(n)]
    T[i][j] = T[0][0] = "X"
    while i!=0 and j != 0:
        if F[i][j] - A[i][j] == F[i-1][j]: #przyszlismy z gory
            T[i-1][j] = "X"
            i-=1
        else: #przyszlismy z lewej
            T[i][j-1] = "X"
            j-=1
    
    while i!=0:
        T[i-1][j] = "X"
        i-=1
    
    while j != 0:
        T[i][j-1] = "X"
        j-=1
    
    return T


def trasa(F,A,i,j): #robi trase na zasadzie listy indeksow
    if i == 0 and j == 0: return [(0,0)]
    if i != 0 and F[i][j] - A[i][j] == F[i-1][j]: #przyszlismy z gory
        return trasa(F,A,i-1,j) + [(i,j)]
    else: return trasa(F,A,i,j-1) + [(i,j)] #przyszlismy z lewej

T = [
    [1,2,3,4,5],
    [9,2,9,4,5],
    [2,6,4,5,6],
    [4,7,5,9,3],
    [9,8,5,1,1],
]

val, resTab = szachyMachy(T)
print(val)
for row in resTab:
    print(row)