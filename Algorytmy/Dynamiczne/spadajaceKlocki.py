#f(i) - najdluzszy ciag klockow konczacy sie na i-tym

def klocki(A): #a-tablica krotek klockow (poczatek,koniec)
    n = len(A)
    F = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[j] + 1, F[i])
    
    maxHeight = max(F)
    res = n - maxHeight #rezultat to tyle ile usuwamy
    return res


A = [(0,10),(1,9),(0,3),(4,5),(0,3),(1,2)]
print(klocki(A))