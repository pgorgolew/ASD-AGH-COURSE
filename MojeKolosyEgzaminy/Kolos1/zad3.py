# Paweł Gorgolewski
# Tworzymy k tablic, które beda zawierac liczby z podanych przedzialow
# beda one zawierac takze n*c elementow
# sortujemy je bucket sortem bo wiemy ze maja jednostajny przedzial
# nastepnie nalezy scalic k-posortowanych list

from zad3testy import runtests
from math import floor

def BucketSort(T,valMax,valMin):
    # m to liczba kubełków oraz liczba elementów
    #valMac - MAX, valMin - MIN
    m = len(T)
    B = [[] for _ in range(m)]
    for i in range(m): #wrzucamy liczby do odpowiednich kubełków
        if T[i] == valMax:
            d=m-1
        else:
            d = floor((T[i] - valMin)/(valMax-valMin) * m)
        B[d].append(T[i]) 

    for i in range(m): #sortuj kubełki
        B[i] = InsertionSort(B[i])

    k = 0
    for i in range(m):
        for b in B[i]:
            T[k] = b
            k += 1

    return T
    
def InsertionSort(tab):
    n = len(tab)
    for i in range(1,n): 
        index = i
        number = tab[index]
        while index > 0 and number < tab[index-1]:
            tab[index], tab[index-1] = tab[index-1], tab[index]
            index -= 1
        
    return(tab)

def SortTab(T,P):
    k = len(P)
    n = len(T)
    K = [[] for _ in range(k)]
    for i in range(n): #rozkładamy liczby na osobne tablice O(n)
        for j in range(k):
            if T[i] >= P[j][0] and T[i] <= P[j][1] and len(K[j]) < int(n*P[j][2]):
                K[j].append(T[i])
                break
    
    # teraz sortujemy bucket sortem nasze osobne tablice
    for i in range(k):
        K[i] = BucketSort(K[i], P[i][1], P[i][0])

    
    z = 0
    for i in range(k):
        for j in range(len(K[i])): 
            T[z] = K[i][j]
            z += 1
    # to jest błędne - brak czasu
    # należy tutaj scalić k-posortowanych tablic
    # gdyby przedziały nie nachodziły się to usunelibysmy warunek 3-ci warunej z 50 linijki
    # i działało by

    return 

runtests( SortTab )

# złożoność czasowa:
# robimy bucket sorta dla łącznej długości tablicu równej n -> O(n)
# Po kolei wrzucamy do T elemnty z kubełków O(n)

# złożoność pamięciowa O(n)
# złożoność czasowa O(n)
