from random import randint
from time import time

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
    
def buildHeap(T):
    n = len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,n,i)

    """HeapInsert(104,T)
    HeapInsert(0,T)
    HeapInsert(-200,T)"""

def HeapSort(T):
    buildHeap(T)
    n = len(T)
    for i in range(n-1,0,-1):
        T[0],T[i] = T[i], T[0] #najwiekszy na koniec tablicy
        heapify(T,i,0) #naprawiamy dla i elementów -> T[0] znowu max

def HeapInsert(val,T): #wstaw na koniec, przesuwaj w gore gdy parent < val
    T += [val]
    n = len(T)
    i = n-1
    while i > 0:
        p = parent(i)
        if T[i] > T[p]:
            T[i], T[p] = T[p], T[i]
            i = p
        else: break

def getMax(T): #with deleting it
    n = len(T)
    val = T[0]
    T[n-1], T[0] = T[0], T[n-1]
    T = T[:n-1]
    heapify(T,n-1,0)
    return val


tab = [randint(-100,150) for _ in range(100)]

start = time()
HeapSort(tab)
end = time()
print(end-start)
print(tab)