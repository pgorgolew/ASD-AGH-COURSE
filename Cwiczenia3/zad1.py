from random import randint

def quicksort3(T,l,r): #teraz gwarantujemy logn zuzytej pamieci
    while l<r:
        q = randPartition(T,l,r)
        if q - l < r - q:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            quicksort3(T,l,q-1)
            l = q+1
        else:
            quicksort3(T,q+1,r)
            r = q-1

def randPartition(T,l,r):
    d = randint(l,r)
    T[r], T[d] = T[d], T[r] #Nasz pivot jest na początku, oraz jest randomowy
    return partition(T,l,r)

def partition(T,l,r):
    x = T[r]
    i=l-1 #Bo na początku mamy 0 liczb <= x
    for j in range(l,r):
        if T[j] <= x:
            i+=1
            T[i],T[j] = T[j], T[i]
        
    T[i+1], T[r] = T[r], T[i+1]

    return i+1 