class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

def insertToFront(first,newVal):
  new_elem=Node(newVal)
  new_elem.next = first
  return new_elem
   	 

def del_max(first):
    if first == None:
        return first
    max_prev = q_prev = None
    max_val = q = first
    while q != None:
        if q.val > max_val.val:
            max_prev,max_val = q_prev, q
        q_prev = q
        q = q.next

    if max_prev == None:
        return first.next, max_val.val

    if max_val.next is None:
        max_prev.next = None
    else:
        max_prev.next = max_val.next
    return first, max_val.val

def selectionSort(first):
    q = first
    i=0
    while q != None:
        q = q.next
        i+=1
    
    if i <= 1: return first
    Sort_First = None
    for j in range(i):
        first, MaxVal = del_max(first)
        Sort_First = insertToFront(Sort_First, MaxVal) 
    
    return Sort_First

#TO JEST DO PIZDY NIE UZYWAJ TEGO