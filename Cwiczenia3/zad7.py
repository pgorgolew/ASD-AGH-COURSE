from random import randint

def HoraePartition(T,l,r):
    mid = (l+r)//2
    pivot = T[mid]
    i = l-1
    j = r+1
    while True:
        i+=1
        while(T[i] < pivot):
            i+=1
        
        j-=1
        while(T[j] > pivot):
            j-=1
        
        if (i>=j):
            return j
        
        T[i], T[j] = T[j], T[i]


def quicksort(T,l,r): #Standard algo
    if l<r:
        q = HoraePartition(T,l,r)
        quicksort(T,l,q)
        quicksort(T,q+1,r)

tab = [randint(0,100) for _ in range(10)]

print(tab)
quicksort(tab,0,len(tab)-1)

print(tab)