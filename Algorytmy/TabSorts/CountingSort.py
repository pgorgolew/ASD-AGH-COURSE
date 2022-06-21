def countingsort(tab):
    k = max(tab)
    n = len(tab)
    countTab = [0 for _ in range(k+1)]
    output = [0 for _ in range(n)]

    for x in tab:
        countTab[x] += 1  #countTab[i] zawiera ilosc wystopien i
    
    for i in range(1,k+1):
        countTab[i] += countTab[i-1] #countTab[i] zaweira pozycje w posortowanej talbicy
                                     #ostatniego elementu o kluczu i
    for i in range(n-1, -1, -1):
        output[countTab[tab[i]]-1] = tab[i] #wstawia element tab[i] na odpowiednia pozycje
        countTab[tab[i]] -= 1  #aktualizuje countTab (Zeby kolejne wywolanie dalo id - 1)

    return output


tab = [10, 8, 10, 5, 11, 7, 1,0,4]
tab = countingsort(tab)
print(tab)