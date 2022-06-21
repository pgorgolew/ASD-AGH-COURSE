from math import log10

def radixsort(tab, k):#k to ilosc cyfr najwiekszej liczby
    n = len(tab)
    #minV = min(tab)
    #for i in range(n):
    #    tab[i] -= minV

    #k = int(log10(max(tab))) + 1
    for i in range(k): #porównujemy dla kazdjec cyfry
        countTab = [0 for _ in range(10)] #10 różnych cyfr, generalnie countingsort
        for j in tab:
            d = digit(j,i)
            countTab[d] += 1
        
        for j in range(1,10):
            countTab[j] += countTab[j-1] #countTab[i] zaweira pozycje w posortowanej talbicy
                                         #ostatniego elementu o kluczu j

        outputs = [tab[i] for i in range(n)]
        for j in range(n-1, -1, -1):
            d = digit(tab[j], i)
            outputs[countTab[d]-1] = tab[j] 
            countTab[d] -= 1 
        
        for j in range(n):
            tab[j] = outputs[j]

    #for i in range(n):
    #     tab[i] += minV

def digit(num, power):
    exp = 10 ** power
    num //= exp
    num %= 10
    return num

tab = [50,100,23,519,723,100,512,51,59]
radixsort(tab, 3)
print(tab)

#O(n) to k*(n+10)      k-ile cyfr w najwiekszej liczbie, 