class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

def insertionSortNode(first): #O(n^2)
    if first == None or first.next == None: return first
    war = Node()
    war.next = first
    prev,q=first,first.next
    while q != None:
        p,prevp = war.next,war #idziemy od początku i szukamy miejsca dla q
        while p!=q and p.val<q.val:
            p,prevp = p.next,p
        
        if p!=q: #q wrzucamy pomiedzy prevp a p
            prev.next = q.next
            prevp.next = q
            q.next = p
            q = prev.next
        else: #q zostaje na swoim miejscu
            prev,q = q,q.next
    
    return war.next