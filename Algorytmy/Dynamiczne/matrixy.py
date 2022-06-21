#F[i][j] - optymalny koszt połączenia macierzy od i do j

# Macierz n x m ma n-wierszy i m-kolumn
# zał, tablica A = [(n, m), ...] gdzie m, n to wielkosc macierzy
# koszt wymnozenia macierzy [n x m] oraz [m x k] to m*n*k (tyle mnozen bedzie)


def macierze(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]

    for o in range(1,n): #odstep miedzy i,j
        for p in range(n-o): #wartosci dla i
            i = p
            j = i + o
            T = [F[i][i+k] + F[k+i+1][j] + A[i][0]*A[i+k][1]*A[j][1] for k in range(o)] #mamy "o" roznych kombinacji od i do j
            F[i][j] = min(T)

    return F[0][n-1]

A = [(30,35),(35,15), (15,5), (5,10), (10,20), (20,25)]
T1 = [[10,100],[100,10],[10,1000]] 
T2 = [[2,3],[3,6],[6,4],[4,5]] 
T3 = [[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]] 
T4 = [[10,100],[100,5],[5,50]]
T5 = [[100,5],[5,50],[10,100]]
# print(macierze(A))
#print(macierze(T1))
#print(macierze(T2))
print(macierze(T3))
print(macierze(T4))
print(macierze(T5))
