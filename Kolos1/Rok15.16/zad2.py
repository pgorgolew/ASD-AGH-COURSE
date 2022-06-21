from math import ceil,log2
from random import randint

def partition(T,l,r):
    x = T[r]
    i=l-1 #Bo na początku mamy 0 liczb <= x
    for j in range(l,r):
        if T[j] <= x:
            i+=1
            T[i],T[j] = T[j], T[i]
        
    T[i+1], T[r] = T[r], T[i+1]

    return i+1 

def randPartition(T,l,r):
    d = randint(l,r)
    T[r], T[d] = T[d], T[r] #Nasz pivot jest na początku, oraz jest randomowy
    return partition(T,l,r)

def quicksort3(T,l,r): #teraz gwarantujemy logn zuzytej pamieci
    while l<r:
        q = randPartition(T,l,r)
        if q - l < r - q:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            quicksort3(T,l,q-1)
            l = q+1
        else:
            quicksort3(T,q+1,r)
            r = q-1
    return T

def sortLog2Change(T,n):
    even = ceil(log2(n))
    odd = n - even
    evenTab = [0]*even 
    oddTab = [0]*odd

    e = o = 0
    for num in T: #O(n)
        if num%2 == 1:
            oddTab[o] = num
            o+=1
        else:
            evenTab[e] = num
            e+=1
    
    #teraz mamy posortowaną oddTab i nieposortowaną evenTab
    evenTab = quicksort3(evenTab,0,even-1) #O(logn*log(logn)) < O(n)

    #teraz mamy posortowaną oddTab i evenTab

    e = o = k = 0
    while e < even and o < odd:  #przepisywanie w O(n)
        if evenTab[e] < oddTab[o]:
            T[k] = evenTab[e]
            e += 1
        else:
            T[k] = oddTab[o]
            o += 1

        k += 1

    while e < even:
        T[k] = evenTab[e]
        e+=1
        k+=1

    while o < odd:
        T[k] = oddTab[o]
        o+=1
        k+=1 
    
    return T # sumarycznie ~ O(n)

n = 10
T = [1,3,20,9,0,30,19,21,4,29]
T = sortLog2Change(T,n)
print(T)