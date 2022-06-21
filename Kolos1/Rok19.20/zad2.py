from random import randint

# Quickselect korzysta z randomowego piviota, który działa dobrze, 
# lecz może trafić na pesymistyczne przypadki. W celu zagwarantowania O(n) należałoby użyć
# magicznych piątek. Dodatkowo zakładam, że wzrosty są parami różne
# Gdyby nie były parami różne to należałoby użyć 3-way-partiton (dzieli tab na <,=,>)
# zakładam że pozycje p i q oznaczają indeksy w tablicy

def select(T,k,l,r):
    n = len(T)
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

def selection(T,p,q):
    n = len(T)
    select(T,p,0,n-1)
    select(T,q,p,n-1)
    return T[p:q+1]


T=[1584,24,15,147,369,8,1,7,155,741]
tab = selection(T,3,9)
print(tab)


# 2x select: 2*c*n, gdzie 2c to stała
# zatem złożonośc czasowa ~ O(n)