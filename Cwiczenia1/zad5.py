class Node:
    def __init__(self, value=None, next=None):
   	 self.value = value
   	 self.next = next
   	 
def printList(first):
    while first != None:
        print(first.value, end=" -> ")
        first = first.next 
    print("None")

def reverse(first):
    prev = None
    q = first
    while q != None:
        p = q.next
        q.next = prev
        prev, q = q, p
    
    return prev


first = Node(1, Node(3, Node(42, Node(63, Node(73, Node(93, None))))))
printList(first)
printList(reverse(first))