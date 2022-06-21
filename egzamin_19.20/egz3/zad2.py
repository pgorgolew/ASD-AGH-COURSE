from zad2testy import runtests

def tower(A):
  #f(i) - najdluzszy ciag klockow konczacy sie na i-tym
    n = len(A)
    F = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[j] + 1, F[i])
    
    maxHeight = max(F)
    res = maxHeight #rezultat to tyle ile usuwamy
    return res


runtests( tower )
