def sort(tab,extraTab,l,r):
    if r - l  > 0: #jezeli jest weicej niz jeden element
        mid = (r+l)//2
        sort(tab,extraTab,l,mid)
        sort(tab,extraTab,mid+1,r)

        i = j = k = 0
        while i < mid-l+1 and j < r - mid:
            if tab[l+i] < tab[mid+1+j]:
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

print(mergesort([4,6,12,4,2,97,4,11,0,62,6,34,72345,1,247,2,512,643,23,7,2,11,5,731,13,4]))