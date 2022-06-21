from random import randint
#Uzywam randomowego pivota jednak da sie zagwarantować brak pesymistycznego przypadku
#używając magicznych piątek, zakładam, że nie będzie takiego przypadku dla randomowego

def quicksort(T,l,r): #teraz gwarantujemy logn zuzytej pamieci
    while l<r:
        q = randPartition(T,l,r)
        if q - l < r - q:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            quicksort(T,l,q-1)
            l = q+1
        else:
            quicksort(T,q+1,r)
            r = q-1
    return T

def partition(T,l,r):
    x = T[r]
    i=l-1 #Bo na początku mamy 0 liczb <= x
    for j in range(l,r):
        if T[j] <= x:
            i+=1
            T[i],T[j] = T[j], T[i]
        
    T[i+1], T[r] = T[r], T[i+1]

    return i+1 

def randPartition(T,l,r):
    d = randint(l,r)
    T[r], T[d] = T[d], T[r] #Nasz pivot jest na początku, oraz jest randomowy
    return partition(T,l,r)

def find_sum(T,index,n):
    x = T[index]

    if index != 0: l = 0
    else: l = 1

    if index != n-1: p = n-1
    else: p = n-2

    while l < p:
        if T[l] + T[p] == x: return True
        elif T[l] + T[p] > x:
            p-=1
            if p == index: p-=1
        else:
            l+=1
            if l == index: l+=1
    
    return False

def check(T):
    n = len(T)
    if n<3: return False

    T = quicksort(T,0,n-1) #nlogn
    for i in range(n):
        if not find_sum(T,i,n): return False
    
    return True

T=[0,0,0,1,1,2,3,0,5,15,10,8]
print(check(T))