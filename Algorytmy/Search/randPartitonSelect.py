from random import randint
#O(n)
def select(T,k): #k to numer liczby, nie indeks
    k -=1
    n = len(T)
    l = 0
    r = n-1
    if k == l: return min(T)
    if k == r: return max(T)
    while True:
        p = randPartition(T,l,r)
        if p==k:
            return T[p]
        elif p > k: #bierzemy lewą część
            r = p-1
        else: #bierzemy prawą część
            l = p+1
    
def randPartition(T,l,r):
        d = randint(l,r)
        T[r], T[d] = T[d], T[r] #Nasz pivot jest na końcu, oraz jest randomowy
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
