# A - sprawdzana tablica
def lisN2(A):
    n = len(A)
    F = [1]*n #najdl podciag konczacy sie na i-tym
    P = [-1]*n  #indeksy do poprzednich wartosci z podciagu
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[j]+1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    
    maxID, maxS = 0,F[0]
    for i in range(1,n):
        if maxS < F[i]:
            maxID, maxS = i, F[i]
            
    return maxS, maxID, P

def printsolution(A,P,i):
    if P[i] != -1:
        printsolution(A,P,P[i])
    print(A[i], end=" ")

def binarySearch(T,x,l,r, lastId):
    while r-l > 1:
        m = (l+r)//2
        if T[lastId[m]] >= x: r = m
        else: l = m
    
    return r

def lis_Nlogn(A): #bez generowania ciagu
    # generalnie najwiekszy mozliwy podciag jest dlugosci n
    # patrzac na kolejne liczby z tablicy A, mamy 3 przypadki
    # 1. liczba > najwiekszej, 2.liczba < najmniejszej, 3.reszta przyapdkow
    # 1) powstaje nowy najdluzszy podciag
    # 2) podciag o 1 el, zostaje zaktualizowany
    # 3) ostatni element odpowiedniego ciagu zostjae "wymieniony na lepsze"

    n = len(A)
    lastId = [0 for _ in range(n)]
    lenght = 1
    P = [-1 for _ in range(n)]
    for i in range(1,n):
        if A[i] > A[lastId[lenght-1]]: #case 1
            P[i] = lastId[lenght-1]
            lastId[lenght] = i
            lenght += 1
        elif A[i] < A[lastId[0]]: #case 2
            lastId[0] = i
        else:
            x = binarySearch(A,A[i],0,lenght-1,lastId)
            P[i] = lastId[x-1] #-1 bo szukamy elementu przed aktualnym
            lastId[x] = i

    
    return lenght, P, lastId[lenght-1]



T = [1,13,7,21,42,8,2,44,53]
# maxS, maxID, P = lisN2(T)
# print(maxS)
# printsolution(T,P,maxID)
res, P, i = lis_Nlogn(T)
print(res)
printsolution(T,P,i)