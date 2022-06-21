from random import randint
from time import time

def quicksort(T,l,r): #Standard algo
    if l<r:
        q = partition(T,l,r)
        quicksort(T,l,q-1)
        quicksort(T,q+1,r)

def quicksort2(T,l,r): #usunięty ogon rekursji (recursion tail)
    while l<r:
        q = partition(T,l,r)
        quicksort2(T,l,q-1)
        l = q+1

def quicksort3(T,l,r): #teraz gwarantujemy logn zuzytej pamieci
    while l<r:
        q = randPartition(T,l,r)
        if q - l < r - q:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            quicksort3(T,l,q-1)
            l = q+1
        else:
            quicksort3(T,q+1,r)
            r = q-1
    return T

def hoarePartition(T,l,r):
    mid = (l+r)//2
    pivot = T[mid]
    i = l-1
    j = r+1
    while True:
        i+=1
        while(T[i] < pivot):
            i+=1

        j-=1
        while (T[j] > pivot):
            j-=1
        
        if (i>=j):
            return j

        T[i],T[j] = T[j], T[i]

def quicksortHoare(T,l,r): #teraz gwarantujemy logn zuzytej pamieci
    while l<r:
        q = hoarePartition(T,l,r)
        if q - l < r - q:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            quicksort3(T,l,q)
            l = q+1
        else:
            quicksort3(T,q+1,r)
            r = q
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

def threeWayQuicksort(T,l,r):
    while l<r:
        left,right = threeWayPartition(T,l,r) #left - koniec lewej czesci, right - poczatek prawej
        if left - l < r - right:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            threeWayQuicksort(T,l,left)
            l = right
        else:
            threeWayQuicksort(T,right,r)
            r = left

    return T

def threeWayPartition(T,l,r): #3 groupy [<,=,>] z random pivot
    if l>=r: return

    d = randint(l,r)
    T[l], T[d] = T[d], T[l] #Nasz pivot jest na początku, oraz jest randomowy
    x = T[l]
    ll = l
    i = l+1 #i to iterator, l to id dla nastepnego elementu < od pivota
    rl = r
    while i<=rl:
        if x > T[i]:
            T[ll], T[i] = T[i], T[ll]
            i+=1
            ll+=1
        elif x == T[i]: i+=1 
        else:
            T[i], T[rl] = T[rl], T[i]
            rl-=1

    return ll-1,rl+1







##########################################################################
# random test sort
from random import randint, seed
from time import time
def test_sort():
  
  rr = (-10**6, 10**6)
  n = 10**5*2
  m = 1
  sort_func = threeWayQuicksort
  print_res = False

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = sort_func(t,0,n-1)
    stop = time()
    if print_res: print('output:  ', t)

    res = '\033[91mINCORRECT\033[0m'
    if t == expected_res:
      res = '\033[92mCORRECT\033[0m'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

    if res == '\033[91mINCORRECT\033[0m':
      break

test_sort()
