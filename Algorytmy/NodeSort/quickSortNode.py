from random import randint, seed

class Node:
  def __init__(self,val=None,next=None):
    self.next = next
    self.value = val
    
def sort(LeftW,RightW=None): # O(nlogn)
  pivot = LeftW.next
  q = pivot.next
  prev = pw = pivot 
  #pw to pierwszy Node, pivot ostatni, których wartość == pivot.value
  #będą wartownikami dla nastepnych wywołań funkcji sort 
  while q != RightW: 
    if pivot.value > q.value: #wstawiamy q przed Lewego Wartownika
      prev.next = q.next
      q.next = LeftW.next
      LeftW.next = q
      q = prev.next

    elif pivot.value < q.value: #zostawiamy
      prev = q
      q = q.next

    else:   #wstawiamy q przed aktualnego pivota, zmieniamy pivota na pivot.next
      prev.next = q.next
      q.next = pivot.next
      pivot.next = q
      q = prev.next

      if prev == pivot: #q i prev wskazywałyby cały czas na te same Nody
        #przyklad:  X -> 4 -> 4 -> X, gdzie X to wartownicy,
        #pierwsza czwórka to prev i zarazem pivot, druga czwórka to q
        q = q.next
        prev = prev.next

      pivot = pivot.next

  if LeftW.next != pw and LeftW.next.next != pw:   
    sort(LeftW,pw)
  if pivot.next != RightW and pivot.next.next != RightW:
    sort(pivot,RightW)

  return LeftW.next

def qsort( L ):
  if L == None or L.next == None: 
    return L 

  LeftW = Node() #Wartownik
  LeftW.next = L 
  L = sort(LeftW)

  return L


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
  
  rr = (-10**3, 10**3)
  n = 10**6//2
  m = 4
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

