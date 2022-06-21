from random import randint

def IterationMerge(tab):
    def sort(T,m):
        L = T[:m]
        R = T[m:]

        nL, nR = len(L), len(R)
        i = j = z = 0
        while i < nL and j < nR:
            if L[i] < R[j]:
                T[z] = L[i]
                i += 1
            else:
                T[z] = R[j]
                j += 1
            z += 1

        while i < nL:
            T[z] = L[i]
            i += 1
            z += 1

        while j < nR:
            T[z] = R[j]
            j += 1
            z += 1
        
        return T
        
    n = len(tab)
    if n <= 1: return tab

    k=2
    while k < n:
        for i in range(0,n,k):
            T = tab[i:i+k]
            middle = k//2
            sort(T,middle)
            for j in range(k):
                if i+j >= n : break #Gdy ostatnia podtablica < k
                tab[i+j] = T[j]

        k+=k
    
    return sort(tab,k//2)



T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = IterationMerge(T)
print("po sortowaniu    : T =", T)
for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")
    
    

