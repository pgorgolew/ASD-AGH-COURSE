def binarySearch(T,x,l,r, lastId): 
    while r-l > 1:
        m = (l+r)//2
        if T[lastId[m]] >= x: r = m
        else: l = m
    
    return r

def lis_Nlogn(A):
    # w lastId beda przetrzymywane takie indeksy elementow, ze lastId[i] bedzie zawierac indeks 
    # do aktualnie najlepszego elementu, ktory konczy ciag o dlugosci i+1
    # nowy element jest potencjalnie lepszy od starego, gdy jest od niego mniejszy, poniewaz 
    # pozniej byc moze uda mu sie stworzyc najdluzszy podciag

    # najwiekszy mozliwy podciag jest dlugosci n
    # patrzac na kolejne liczby z tablicy A, mamy 3 przypadki
    # 1. liczba > najwiekszej, 2.liczba <= najmniejszej, 3.reszta przypadkow
    # 1) powstaje nowy najdluzszy podciag (lastId[length])
    # 2) podciag o dlugosci 1 zostaje zaktualizowany (lastId[0])
    # 3) ostatni element odpowiednio dlugiego ciagu zostaje "wymieniony na potencjalnie lepszy" 
    
    n = len(A)
    lastId = [0 for _ in range(n)] 
    length = 1
    P = [-1 for _ in range(n)] 
    # P[i] zawiera indeks do ostatniego (bo nie musi to byc jedyny) elementu poprzedzajacego i-ty w podciagu
    F = [1 for _ in range(n)] #F[i] najdluzszy, podciag konczacy sie na elemencie o indeksie i

    for i in range(1,n):
        if A[i] > A[lastId[length-1]]:  #przypadek 1)
            P[i] = lastId[length-1]
            lastId[length] = i
            length += 1
            F[i] = length
        elif A[i] <= A[lastId[0]]:      #przypadek 2)
            lastId[0] = i
        else:                           #przypadek 3)
            x = binarySearch(A,A[i],0,length-1,lastId) # x - indeks do lastId, dla A[i]
            P[i] = lastId[x-1] 
            lastId[x] = i 
            F[i] = x+1 #x to indeks w lastId, zatem faktyczna dlugosc tego ciagu to x+1
    
    # Wyjasnienie: P[i] = lastId[t-1]
    # t+1 - najdluzszy ciag jaki stworzy sie z itym elementem na koncu, t - pozycja w lastId
    # rodzicem i-elementu musi byc aktualnie najlepszy element, ktory tworzy ciag o dlugosci t -> lastId[t-1]
    return length, P, lastId[length-1], F

def printArr(T):
    n = len(T)
    for i in range(n-1,-1,-1): #tablica zawiera odwrocana kolejnosc podciagu
        print(T[i], end=" ")
    print("")

def printAllLIS(A):
    def createAll(A,P,F,i,l,res=[]):
        nonlocal licznik
        # l - dlugosc ciagu jaki jest aktulanie rozwazany
        # P - tablica parents, przydatna, bo pokazuje pierwszego rozwazanego rodzica
        # i - aktualny indeks w tablicy
        # F[i] - dlugosc najdluzszego ciagu konczacego sie na itym elemencie
        if l == 0:
            printArr(res)
            licznik +=1
            return
        
        createAll(A,P,F,P[i],l-1,res+[A[i]])
        #po wypisaniu podciagu stworzonego dzieki P[], nalezy znalezc kolejne elementy tworzace ciag rosnacy

        current = float("inf") if res==[] else res[-1] #trzeba zapewnic, ze parent jest mniejszy
        for k in range(i-1,l-2,-1): # l-2 bo musi zostac l-1 elementow aby powstal ciag
            if F[k] == l and A[k] < current: createAll(A,P,F,P[k],l-1,res+[A[k]])
    
    licznik = 0
    length, P, i, F = lis_Nlogn(A)
    createAll(A,P,F,i,length) 
    print(licznik)