#zadanie "wybor z terminami"

def heapify(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] > T[m]: m = l
    if r < n and T[r] > T[m]: m = r
    if m != i:
        T[m], T[i] = T[i], T[m]
        heapify(T,n,m)

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

def HeapInsert(val,T,n): #wstaw na koniec, przesuwaj w gore gdy parent < val
    i = n-1
    T[i] = val
    while i > 0:
        p = parent(i)
        if T[i] > T[p]:
            T[i], T[p] = T[p], T[i]
            i = p
        else: break

def getMax(T,n):
    val = T[0]
    T[n-1], T[0] = T[0], T[n-1]
    heapify(T,n-1,0)
    return val

def tasks(T):
    #zal, ze T[i] = [deadline, zysk]
    T = sorted(T, key = lambda x: x[0])
    n = len(T)
    tab = [0]*n
    l=0 #aktualna dlugosc tab
    s = 0
    maxDeadline = T[n-1][0]
    i = n-1
    while i >= 0:
        while maxDeadline == T[i][0]:
            l+=1
            HeapInsert(T[i][1],tab,l)
            i-=1

        maxDeadline -= 1
        if l > 0:
            s += getMax(tab,l)
            l-=1
    
    return s

T=[[1, 10], [2,7], [2,20],[1,9],[5,10],[5,1],[4,4]]
print(tasks(T))


