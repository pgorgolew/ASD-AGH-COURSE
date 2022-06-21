class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class TwoLists:
    def __init__(self):
        self.even = None
        self.odd = None

def TwoListsSort(first):
    evenAndOdd = TwoLists()
    o = e = None
    q = first
    while q!=None:
        if q.value % 2 == 0:
            if e == None:
                evenAndOdd.even = q
                e = evenAndOdd.even
            else:
                e.next = q
                e = e.next
        else:
            if o == None:
                evenAndOdd.odd = q
                o = evenAndOdd.odd
            else:
                o.next = q
                o = o.next
        
        q = q.next

    e.next = None
    o.next = None
    return evenAndOdd

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

T = [1,6,78,12,4,121,57,32,22,46,9]
first = array_to_list(T)
result = TwoListsSort(first)
even,odd = result.even, result.odd
even, odd = list2tab(even), list2tab(odd)
print(even)
print(odd)