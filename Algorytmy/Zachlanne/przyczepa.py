#algorytm zachłanny
def przyczepa1(K,W):
    #tutaj wagi mamy w potęgach 2
    W = sorted(W) #mozna counting sortem
    n = len(W)

    w = 0 #aktualna waga
    z = 0 #
    for i in range(n-1,-1,-1):
        if w + W[i] <= K:
            w += W[i]
            z += 1
    
    return z, w

def przyczepa2(K,W):
    #W są dowolne
    #F(i,j) - minimalna ilosc ladunkow (do i) ktora wazy j
    n = len(W)
    F=[[float("inf")]*(K+1) for _ in range(n+1)]
    F[0][0] = 0
    F[0][W[0]] = 1
    for i in range(1,n+1):
            for j in range(K+1):
                k = i-1
                # jezeli sie dalo osiagnac to bez i-tego przedmiotu to bedzie liczba, inaczej inf
                F[i][j] = F[k][j]
                if j-W[k] >= 0: F[i][j] = min(F[i][j], F[k][j-W[k]] + 1)
    

    for j in range(K,-1,-1):
        if F[n][j] != float("inf"):
            return F[n][j], j
            

W = [2, 2, 4, 8, 16, 8, 1]
K = 27
print(przyczepa2(K,W))