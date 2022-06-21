# Paweł Gorgolewski

# quickselectem znajdujemy pierwszą i ostatnią mediane dzieki czemu sortuje nam sie tablica
# partition działa tak, jakby chciał posortować malejąco
# Następnie zamieniam zamieniam mediany z odpowiednimi liczbami na przekątnych
# w niektórych przypadkach wymieniam również inne elementy
from zad1testy import runtests
from random import randint

#w tym selecie traktujemy tablice dwuwymiarową jako jednowymiarową
# dodatkowo zmieniam funkcje tak, aby układały liczby malejąco
def select(T,k,l,r): #k to indeks liczby
    n = len(T)
    if k == l: return 
    if k == r: return 
    while True:
        p = randPartition(T,l,r)
        if p==k:
            return 
        elif p < k: #bierzemy prawą część
            l = p+1
        else: #bierzemy prawą część
            r = p-1
    
def randPartition(T,l,r):
        n = len(T)
        d = randint(l,r)
        T[r//n][r%n], T[d//n][d%n] = T[d//n][d%n], T[r//n][r%n] #Nasz pivot jest na końcu, oraz jest randomowy
        return partition(T,l,r)

def partition(T,l,r):
    n = len(T)
    x = T[r//n][r%n]
    i=l-1 #Bo na początku mamy 0 liczb >= x
    for j in range(l,r):
        if T[j//n][j%n] >= x:
            i+=1
            T[i//n][i%n], T[j//n][j%n] = T[j//n][j%n], T[i//n][i%n]
        
    T[(i+1)//n][(i+1)%n], T[r//n][r%n] = T[r//n][r%n], T[(i+1)//n][(i+1)%n]

    return i+1 


# Dla tablicy NxN tablica jednowymiarowa miałaby n^2 elemnetów
# N elementów musi być na przekątnej - będą to mediany
# zostaje nam n^2-n = n*(n-1) elementów mniejszych i większych
# ostatni z najmnijeszych to n*(n-1)//2 element -> ma indeks n*(n-1)//2 - 1
# zatem nasza pierwsza mediana bedzie miała indeks n*(n-1)//2 zaś ostatnia n*(n-1)//2 + n-1
def Median(T):
    n = len(T)
    firstM = n*(n-1)//2
    lastM = firstM + n-1
    select(T,firstM,0,n*n-1)
    select(T,lastM,firstM+1,n*n-1)
    #indeksy od 0 do firstM - 1 -> elementy które powinny być nad przekątną (bo są wieksze od median)
    #indeksy od firstM do lastM -> te powinny być na przekątnej
    #reszta powinna być pod przekątną (bo sa mneijsze od median)

    if n%2 == 1: 
        #dla nieparzystych n, mediany znajdują się w n//2 wierszu
        w = n//2
        for k in range(n-1,-1,-1):
            if n == n//2: continue #bo ta mediana na swoim miejscu
            medID = (n-1) - k
            T[w][k], T[medID][medID] = T[medID][medID], T[w][k]
            #zamieniamy mediany z elementami znajdujacymi sie na przekatnych
            # tak zeby spelnic warunki zadania
    
    else:
        #mediany znajdują się na n//2 ostatnich miejsc wiersza o indeksie n//2-1
        #oraz na n//2 pierwszych miejscach wiersza o indeksie n//2
        w1 = n//2 - 1
        w2 = w1+1
        for i in range(n//2): #tym wrzucamy mediany na swoje miejsca
            T[w1][n//2+i], T[i][i] = T[i][i],T[w1][n//2 + i]
            T[w2][n//2 - 1 - i], T[w2+i][w2+i] = T[w2+i][w2+i], T[w2][n//2 - 1 - i]
        
        #pozostają nam teraz do zamienienia "trójkąty prostokątne" pomiędzy medianą a większymi/mniejszymi
        z = n//2 - 1 #wysokość trójkąta
        for i in range(z,0,-1):
            for j in range(i):
                T[w1][j], T[w2][(n-1)-j] = T[w2][(n-1)-j],  T[w1][j]
            w1 -= 1
            w2 += 1
        
    return

runtests( Median ) 


#Złożoność programu:
# O(n^2) -> szukamy 2 razy quickselectem
# O(n) -> zamieniamy mediany
# O(n) -> w zaleznosci od wielkosci tablicy zamieniamy takze "tzw trójkąty"

#ogólna złożoność O(n^2)
#złożoność pamięciowa O(1) -> stała
