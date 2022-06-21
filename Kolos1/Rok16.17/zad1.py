from math import floor

class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

def insertionSortNode(first):
    if first == None or first.next == None: return first
    war = Node()
    war.next = first
    prev,q=first,first.next
    while q != None:
        p,prevp = war.next,war
        while p!=q and p.val<q.val:
            p,prevp = p.next,p
        
        if p!=q:
            prev.next = q.next
            prevp.next = q
            q.next = p
            q = prev.next
        else: #q zostaje na swoim miejscu
            prev,q = q,q.next
    
    return war.next


def sort(first):
    #first = war.next
    if first == None or first.next == None:
        return first
    A = 10 #max val
    B = 0 #min val

    n=1 #liczba elementow
    q=first.next
    while q!=None:
        q = q.next
        n+=1

    buckets = [Node() for _ in range(n)]
    q = first
    while q != None:
        index = floor(((q.val-B)/(A-B))*n)
        p = q.next
        q.next = buckets[index].next
        buckets[index].next = q
        q = p

    result = q = Node()
    for bucket in buckets:
        bucket.next = insertionSortNode(bucket.next)
        q.next = bucket.next
        while q.next!=None:
            q = q.next

    return result.next


def list2tab(A):
  if A is None:
    return []

  res = []
  while A is not None:
    res.append(A.val)
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
from random import random
from time import time
def test_sort():
  
  rr = (0, 9.99999999999999999999999)
  n = 1000
  m = 10
  sort_func = sort
  print_res = False

  for i in range(m):
    t = [random()*10 for _ in range(n)]
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