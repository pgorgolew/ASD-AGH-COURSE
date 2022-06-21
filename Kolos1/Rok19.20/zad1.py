#tworzymy krotki (liczba, ileJednokronych, ileWielokrotnych)

def count(number): #zwraca liczbe wraz z iloscia jednokrotnych i wielokrotnych
    one = 0 #ilosc jednokrotnych
    more = 0 # ilosc wielokrotnych
    tab = [0]*10
    k = number
    while k > 0:
        digit = k%10
        if tab[digit] == 0: one+=1
        elif tab[digit] == 1:
            one-=1
            more+=1

        tab[digit] += 1
        k//=10
    
    return (number,one,more)

def dataChange(T,n): #zwraca tablice z krotkami (liczba, ileJedn, ileWiel)
    tab=[0]*n
    maxOne = maxMore = 0
    for i in range(n):
        tab[i]=count(T[i])
        maxOne = max(maxOne, tab[i][1])
        maxMore = max(maxMore, tab[i][2])
    return (tab, maxOne, maxMore)

def countingSort(tab,k,f):
    n = len(tab)
    countTab = [0 for _ in range(k+1)]
    output = [0 for _ in range(n)]

    for x in tab:
        countTab[x[f]] += 1  #countTab[i] zawiera ilosc wystopien i
    
    for i in range(1,k+1):
        countTab[i] += countTab[i-1] #countTab[i] zaweira pozycje w posortowanej talbicy
                                     #ostatniego elementu o kluczu i
    for i in range(n-1, -1, -1):
        output[countTab[tab[i][f]]-1] = tab[i] #wstawia element tab[i] na odpowiednia pozycje
        countTab[tab[i][f]] -= 1  #aktualizuje countTab (Zeby kolejne wywolanie dalo id - 1)

    if f==2:
        for i in range(n):
            tab[i] = output[n-1-i]
    elif f==1:
        for i in range(n):
            tab[i] = output[n-1-i][0]  

    return tab

def pretty_sort(T):
    n = len(T)
    T, maxOne, maxMore = dataChange(T,n)
    
    T = countingSort(T,maxMore,2)
    T = countingSort(T,maxOne,1)
    #drugie uzycie countingSorta zwraca posortowane liczby, nie krotki
    return T


T = [3322, 1266, 114577, 123, 455, 2344, 67333, 1234455, 12344, 12, 134, 12, 13, 432, 543, 5434, 22]
T = pretty_sort(T)
print(T)
    
#złożonośc czasowa: ~ O(n):
#Datachange: (n*k) k-> n razy i zalezy od długości liczb
#2xcountingSort: 2*(n+m) [ m<=10 ]
#Po sumowaniu T(n) = n(k+2) + 2m = c*n gdzie c to 