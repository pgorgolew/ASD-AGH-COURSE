class Node:
    def __init__(self, value=None, next=None):
   	 self.value = value
   	 self.next = next

def printList(first):
    while first != None:
        print(first.value)
        first = first.next

def MergeSortNode(first): #O(nlogn)
    def merge(left):
        if left == None or left.next == None:
            return left
        
        newRight = GetMiddle(left)
        newLeft = newRight.next
        newRight.next = None
        first_half = merge(left)
        sec_half = merge(newLeft)
        result = TwoListsToOne(first_half, sec_half)
        return result


    def GetMiddle(first):
        slow = fast = first

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def TwoListsToOne(first_half, sec_half):
        if first_half == None: return sec_half

        elif sec_half == None: return first_half

        war = result = Node()

        while first_half != None and sec_half != None:
            if first_half.value > sec_half.value:
                result.next = sec_half
                result = result.next
                sec_half = sec_half.next
            else:
                result.next = first_half
                result = result.next
                first_half = first_half.next 

        if first_half != None:
            result.next = first_half
        else: result.next = sec_half

        return war.next

    if first == None or first.next==None: return first
    first = merge(first)
    return first
    

##########################################################################
# random test sort linked list

def array_to_list(A):
  head = Node()
  curr = head
  for e in A:
    curr.next = Node(e)
    curr = curr.next

  return head.next

def list_to_array(A):
  if A is None:
    return []

  res = []
  while A is not None:
    res.append(A.value)
    A = A.next

  return res


from random import randint, seed
from time import time
def test_sort():
  rr = (0, 10**3*)
  n = 10**5
  m = 1
  sort_func = MergeSortNode
  print_res = False

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = list_to_array(sort_func(array_to_list(t)))
    stop = time()
    if print_res: print('output:  ', t)

    res = 'INCORRECT'
    if t == expected_res:
      res = 'CORRECT'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

    if res == 'INCORRECT':
      break

test_sort()