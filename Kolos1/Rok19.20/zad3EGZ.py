from math import log,floor
from random import random

def fast_sort(tab,a):
    n = len(tab)
    B = [[] for _ in range(n)]

    for i in range(n): #wrzucamy liczby do odpowiednich kubełków
        if tab[i] == a: 
            d = n - 1
        else:
            x = log(tab[i],a)
            d = floor(x*n)
        
        B[d].append(tab[i])

    for i in range(n): #sortuj kubełki
        B[i] = InsertionSort(B[i])
    
    k = 0
    for i in range(n):
        for b in B[i]:
            tab[k] = b
            k += 1

    return tab 

def InsertionSort(tab):
    n = len(tab)
    for i in range(1,n): 
        index = i
        number = tab[index]
        while index > 0 and number < tab[index-1]:
            tab[index], tab[index-1] = tab[index-1], tab[index]
            index -= 1
        
    return tab


a = 30
T = [a**random() for _ in range(3)]
print(fast_sort(T,a))

