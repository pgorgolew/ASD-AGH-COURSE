from zad1testy import runtests
# Paweł Gorgolewski
# 1) Algorytm tworzy nowa tablice ktora zawiera krotki (liczba, indeks w T)
# 2) Sortuje je mergeSortem poniewaz jest stabilny (dzieki temu dziala pkt 3)
# 3) liniowo sprawdza najwieksza roznice indeksow aktualnej i poprzedniej 
# Znaleziona najwieksza roznica to szukane k

# Zlozonosc czasowa O(nlogn + n)=O(nlogn)
# Zlozonosc pamieciowa O(n+n)=O(n) [jedno z mergesorta, drugie z tworzenia newT]

def sort(tab,extraTab,l,r):
    if r - l  > 0: #jezeli jest weicej niz jeden element
        mid = (r+l)//2
        sort(tab,extraTab,l,mid)
        sort(tab,extraTab,mid+1,r)

        i = j = k = 0
        while i < mid-l+1 and j < r - mid:
            if tab[l+i][0] <= tab[mid+1+j][0]:
                extraTab[l+k] = tab[l+i]
                i+=1
            else:
                extraTab[l+k] = tab[mid+1+j]
                j+=1
            k+=1
        
        while i < mid-l+1:
            extraTab[l+k] = tab[l+i]
            i+=1
            k += 1

        while j < r - mid:
            extraTab[l+k] = tab[mid+1+j]
            j+=1
            k += 1
        
        for i in range(l,r+1):
            tab[i] = extraTab[i]
    
    return tab

def mergesort(tab):
    extraTab = [el for el in tab]
    n = len(tab)
    tab = sort(tab,extraTab,0,n-1)
    return tab

def chaos_index( T ):
    n = len(T)
    newT = [(T[i], i) for i in range(n)]
    newT = mergesort(newT)
    k = 0
    print(newT)
    for i in range(n):
        p = abs(newT[i][1]-i) #potencjalne k
        if p > k: k = p
    return k

runtests( chaos_index )
