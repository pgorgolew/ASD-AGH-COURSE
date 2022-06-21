def MergeSort_1a(tab):
    def series(tab):
        T = []
        i=0
        while i < len(tab):
            sorted = [tab[i]]
            while i+1 < len(tab) and tab[i] <= tab[i+1]:
                sorted += [tab[i+1]]
                i+=1
            
            i+=1
            T += [sorted]
        
        return T
    def merge(L,R):
        tab = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab += [L[i]]
                i += 1
            else:
                tab += [R[j]]
                j += 1

        while i < len(L):
            tab += [L[i]]
            i += 1

        while j < len(R):
            tab += [R[j]]
            j += 1
        
        return tab
    
    sortTab = series(tab)
    
    while True:
        n = len(sortTab)
        if n == 2: return merge(sortTab[0], sortTab[1])
        else:
            tmpTab = []
            for i in range(n//2):
                TwoIn1 = merge(sortTab[2*(i)+1], sortTab[2*i])
                tmpTab += [TwoIn1]

            if n%2 == 1: tmpTab += [sortTab[n-1]]

            sortTab = tmpTab

print(MergeSort_1a([i for i in range(100,0,-1)]))