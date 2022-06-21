#mamy stringi o lacznej dlugosci n, ZAKŁADAM, ŻE Z MAŁYCH LITER
#sortujemy od ostaniego kubełka (najdluzsze slowo) i kolejno sprawdzamy litery na pozycjach
#z indeksem aktualnego kubełka


def radixSortForStrings(tab):
    tab = dataChange(tab)
    h = len(tab) #ile slow
    n = max(word[1] for word in tab) #nadluzsze slowo

    B = [[] for _ in range(n)] #kubełki dla różnej długości słów
    for word in tab: #wypełniamy kubełki
        B[word[1]-1].append(word[0]) 

    for i in range(n-1,-1,-1): #porównujemy dla liter na kazdej pozycji, biorąc i-ty kubełek
        countTab = [0 for _ in range(26)] #ord('a')=97, ord('z')=122
        currTab = B[i]

        for j in currTab:
            l = j[i]
            countTab[ord(l)-97] += 1
        
        for j in range(1,26):
            countTab[j] += countTab[j-1] #countTab[i] zawiera pozycje w posortowanej tablicy
                                         #ostatniego elementu o kluczu j
                                        
        m = len(currTab)
        outputs = [None for _ in range(m)]
        for j in range(m-1, -1, -1):
            l = currTab[j][i]
            outputs[countTab[ord(l)-97]-1] = currTab[j] 
            countTab[ord(l)-97] -= 1 
        
        if i != 0:
            B[i-1] += outputs

    tab = [word for word in outputs]
    return tab

def dataChange(tab):
    for i in range(len(tab)):
        tab[i] = (tab[i],len(tab[i]))
    return tab

check = ['afasdf','sghtjre','wasfwaf','ipoigsnfdv','aoidfpa','poasdfm','a','jnddr']
print(radixSortForStrings(check))

