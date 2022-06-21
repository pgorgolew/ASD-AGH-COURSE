from random import randint
#n^2-1 wartosci
def radixsort(tab):
    n = len(tab)
    for i in range(2): # Kazda liczba jest postaci A*n + B, czyli tak jakbysmy porownywali 2-cyfrowe liczby
        countTab = [0 for _ in range(n)] #n różnych reszt z dzielenia przez n
        for j in tab:
            d = digit(j,i,n)
            countTab[d] += 1
        
        for j in range(1,n):
            countTab[j] += countTab[j-1] #countTab[i] zaweira pozycje w posortowanej tablicy
                                         #ostatniego elementu o kluczu j

        outputs = [tab[i] for i in range(n)]
        
        for j in range(n-1, -1, -1): #sortuje tablice względem "itej cyfry" - pierw B potem A
            d = digit(tab[j], i,n)
            outputs[countTab[d]-1] = tab[j]  
            countTab[d] -= 1 
        
        for j in range(n):
            tab[j] = outputs[j] 

def digit(num, power,n):
    exp = n ** power
    num //= exp
    num %= n
    return num
n=10
tab = [randint(0,n*n-1) for _ in range(n)]
radixsort(tab)
print(tab)

#O(n) 2*(n+n+n+n) = 8n