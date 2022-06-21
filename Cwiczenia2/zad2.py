def Inversion(tab): 
    def mergesort(tab):
        nonlocal count
        if len(tab) > 1:
            mid = len(tab)//2
            L = tab[:mid]
            R = tab[mid:]
            mergesort(L)
            mergesort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    tab[k] = L[i]
                    i += 1
                else:
                    tab[k] = R[j]
                    count+=len(L)-i
                    j += 1
                    
                k += 1

            while i < len(L):
                tab[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                tab[k] = R[j]
                j += 1
                k += 1
        
        return
    
    count = 0
    mergesort(tab)
    return count

print(Inversion([1, 20, 6, 4, 5]))