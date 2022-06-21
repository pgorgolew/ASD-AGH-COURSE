def list2tab(A):
  if A is None:
    return []

  res = []
  while A is not None:
    res.append(A.value)
    A = A.next

  return res  

def array_to_list(A):
  head = Node()
  curr = head
  for e in A:
    curr.next = Node(e)
    curr = curr.next

  return head.next

##########################################################################
# random test sort
from random import randint, seed
from time import time
def test_sort():
  
  rr = (-10**6, 10**6)
  n = 10**6
  m = 10
  sort_func = qsort
  print_res = False

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = list2tab(sort_func(array_to_list(t)))
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
    sort_name = linearselect

    k = randint(0,n-1)
    expected = expected_res[k]

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