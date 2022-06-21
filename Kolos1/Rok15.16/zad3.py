class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def insert(first,newNode):
    newVal = newNode.val
    if first.val > newVal:
        newNode.next = first
        return newNode

    prev = first
    curr = first.next
    while curr != None:
        if curr.val > newVal: break

        prev,curr = curr,curr.next

    prev.next = newNode
    newNode.next = curr
    return first

#zakładam, że zmieniona wartość zepsuła posortowanie
def fixSortedList(first):
    if first.next.val < first.val:
        toInsert = first
        first = first.next
        toInsert.next = None
        q = first

    else:
        q = first.next
        prev = first
        while q.next != None: #O(n)
            if q.val > q.next.val:
                if prev.val > q.next.val: #q.next jest tym złym
                    toInsert = q.next
                    q.next = q.next.next
                else: #q jest tym złym
                    prev.next = q.next
                    toInsert = q
                    q = q.next
                
                toInsert.next = None
                break

            prev,q = q,q.next

    #Mamy posortowaną listę i chcemy wrzucić do niego toInsert

    if q.val <= toInsert.val:
        insert(q,toInsert) #mozemy iterowac dalej
    else:
        first = insert(first,toInsert) #musimy iterowac od nowa

    return first

def array_to_list(A):
  head = Node()
  curr = head
  for e in A:
    curr.next = Node(e)
    curr = curr.next

  return head.next

def list2tab(A):
  if A is None:
    return []

  res = []
  while A is not None:
    res.append(A.val)
    A = A.next

  return res  

T=[1,2,3,4,5,6,7,8,200,100]
first = array_to_list(T)
result = fixSortedList(first)
print(list2tab(result))

    
                

            
