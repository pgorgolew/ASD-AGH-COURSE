# f(i,g,d) - 1 gdy pierwsze i aut mozna rozmiescic na promie tak, ze zostaje 
#            g miejsca na gorze i d miejsca na dole, else 0
# f(i,g,d) = max(n| f(n,g,d) = 1) {iter po n,g,d}
# f(i,g,d) = f(i-1,g + A[i], d) or f(i-1, g, d+A[i]) #g,d oznacza wolne miejsce dlatego +A[i]
def prom(A,L):
    n = len(A)
    F = [[[False]*(L+1) for _ in range(L+1)] for _ in range(n+1)]

    F[0][L][L] = True # bo zero aut i full miejsca

    for i in range(1,n+1): #spr autka po kolei
        k = i-1 #indeks do tablicy dla auta nr i
        for g in range(0,L+1): #minimalne wolne miejsce to 0
            for d in range(0,L+1): #maksymalne wolne miejsce L-A[k]
                if g <= L-A[k]: #zeby nie wyszlo za tablice
                    F[i][g][d] = F[i-1][g+A[k]][d]
                if d <= L-A[k]: #zeby nie wyszlo za tablice
                    F[i][g][d] = F[i][g][d] or F[i-1][g][d+A[k]]

    for i in range(n,-1,-1):
        for g in range(L+1):
            for d in range(L+1):
                if F[i][g][d]: 
                    printsolution(A, F,i,g,d,L)
                    return i

def printsolution(A, F, i, g, d, L): # tworzy string pokazujacy na ktory poklad wjezdzaja dane auta
    s =""
    for k in range(i-1,-1,-1): #bo i to ilosc aut a nie indeksy do A
        z = k+1 #k to indeks w A, z to numer auta w kolejce
        if g+A[k] <= L and F[k][g+A[k]][d]:
            s = f"{z} -> G; " + s
            g += A[k]
        else:
            s = f"{z} -> D; " + s
            d+=A[k]

    print(s)

A=(2,1,3,4)
print(prom(A,5))