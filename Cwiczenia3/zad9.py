from random import randint

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


#################################################
############### TESTER SELECTA ##################
#################################################
from time import time
def test_sort():
  rr = (-1000000,1000000)
  n = 10**5
  m = 5
  print_res = False

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)
    sort_name = select

    k = randint(1,n)
    expected = expected_res[k-1]

    if print_res: 
      print('sorted_input:   ', expected_res)

    start = time()
    q = sort_name(t,k)
    stop = time()
    if print_res: print('output:  ', q, ' expected:  ', expected)

    res = '\033[91mINCORRECT\033[0m'
    if q == expected:
      res = '\033[92mCORRECT\033[0m'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

    if res == '\033[91mINCORRECT\033[0m':
      break

test_sort()