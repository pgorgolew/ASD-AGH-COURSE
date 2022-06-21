#najdluzszy wspolny podciag

#F[i][j] - najdluzszy wspolny podciag stworzony z i-pierwszych wartosci pierwszego slowa i j-pierwszych drugiego

def nwp(A,B):
    n = len(A)
    m = len(B)
    F = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]: #przedłużamy o 1 F[i-1][j-1]
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    return F[n][m]

print(nwp(['a','a','b','d','e','t','q','w'],['a','b','d','d','t','z']))

#f(i,j) = {if ity == joty f[i-1][j-1], else max(f(i-1,j))}