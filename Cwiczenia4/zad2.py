#mamy floor(log(n)) różnych wartości, n elementów w tablicy
from math import log2, ceil
from random import randint

def SearchToInsert(uniq,el,p,last,l=0):
    if el < uniq[l]:
        Insertion(uniq,el,l,last)
        return True

    if el > uniq[p]:
        Insertion(uniq,el,p+1,last)
        return True

    mid = (p+l)//2
    if uniq[mid] > el:
        return SearchToInsert(uniq,el,mid-1,last,l)
    elif uniq[mid] < el:
        return SearchToInsert(uniq,el,p,last,mid+1)
    else: #ten element jest w unique
        return False

def Insertion(uniq,el,index,last):
    uniq[last] = el
    for i in range(last,index,-1):
        uniq[i],uniq[i-1]=uniq[i-1], uniq[i]
    
    return

def binary(tab,el,l,p):
    if l >= p:
        return p

    mid = (l+p)//2
    if tab[mid] > el: return binary(tab,el,l,mid-1)
    elif tab[mid] < el: return binary(tab,el,mid+1,p)
    else: return mid


def sort(tab):
    n = len(tab)
    l = ceil(log2(n))
    uniq = [0 for _ in range(l)] #tu beda unikalne elementy

    uniq[0]=tab[0]
    i = k = 1
    while i < l: 
        if SearchToInsert(uniq,tab[k],i-1,i): i+=1 #log(n)*(log(log(n))
        k+=1
    
    counts = [0 for _ in range(l)]
    for j in range(n):
        index = binary(uniq, tab[j],0,l-1) #n*log(log(n)) (n razy binary search na uniq)
        counts[index] += 1
    
    # p = 0
    # for j in range(l):
    #     for z in range(counts[j]): #n operations
    #         tab[p] = uniq[j]
    #         p+=1
    
    for j in range(1,l):
        counts[j] += counts[j-1]
    
    tmp = [tab[i] for i in range(n)]
    for j in range(n-1,-1,-1):
        k = binary(uniq,tmp[j],0,l-1)
        tab[counts[k]-1] = tmp[j]
        counts[k] -= 1

    return tab



from random import randint, seed
from time import time
def test_sort():
  
  n = 10**5
  rr = (1, ceil(log2(n)))
  m = 5
  sort_func = sort
  print_res = False

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = sort_func(t)
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
    

    

    
    
