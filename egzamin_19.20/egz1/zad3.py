from zad3testy import runtests
import math
# x rozlozone rownomiernie -> bucket sort dla n=len(T) kubelkow
# kubelki wyznaczamy jako floor(math.log(T[i],a) * n)
# poprzez logarytm wyznaczamy x ktory nalezy <0,1>, mnozymy przez liczbe kubelkow
# i robiac floor wyznaczamy nr kubelka do ktorego ma trafic dany element

# zlozonosc O(n) bo bucket sort

def BucketSort(T,a): 
    n = len(T)
    B = [[] for _ in range(n)]
    for i in range(n): #wrzucamy liczby do odpowiednich kubełków
        d = int(math.log(T[i],a) * n)
        if d == n: d-=1 #przypadek gdy t[i] = a
        B[d].append(T[i]) 

    for i in range(n): #sortuj kubełki
        B[i] = InsertionSort(B[i])

    k = 0
    for i in range(n):
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
    
def fast_sort(tab, a):
    return BucketSort(tab,a)

runtests( fast_sort )
