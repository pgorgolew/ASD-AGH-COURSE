from zad3testy import runtests

def heapify(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l][0] < T[m][0]: m = l
    if r < n and T[r][0] < T[m][0]: m = r
    if m != i:
        T[m], T[i] = T[i], T[m]
        heapify(T,n,m)

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

def HeapInsert(val,headID,T): #wstaw na koniec, przesuwaj w gore gdy parent < val
    T.append((val,headID))
    n = len(T)
    i = n-1
    while i > 0:
        p = parent(i)
        if T[i][0] < T[p][0]:
            T[i], T[p] = T[p], T[i]
            i = p
        else: break

def getMin(T): #with deleting it
    n = len(T)
    val = T[0]
    T[n-1], T[0] = T[0], T[n-1]
    T.pop()
    heapify(T,n-1,0)
    return val

def tasks(T):
    n = len(T)
    possible = [True]*n
    heap = []
    for i in range(n):
        HeapInsert(T[i].val, i, heap)
    
    #pierwszy node
    val, x = getMin(heap)
    q = T[x]
    T[x] = T[x].next
    q.next = None
    head = q
    # warunek gdyby byla lista jednoelementowa
    if T[x] is not None: HeapInsert(T[x].val, x, heap)

    #reszta
    while heap:
        val, x = getMin(heap)
        q.next = T[x]
        T[x] = T[x].next
        q = q.next
        q.next = None
        if T[x] is not None: HeapInsert(T[x].val, x, heap)

    return head

runtests( tasks )
