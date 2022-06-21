class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def printList(first):
    while first != None:
        print(first.value)
        first = first.next


def insert(first, newVal):
    if first == None:
        new_elem = Node(newVal)
        return new_elem

    prev = None
    curr = first
    while curr != None:
        if curr.value == newVal: return first
        prev, curr = curr, curr.next

    new_elem = Node(newVal)
    prev.next = new_elem
    return first


def del_max(first):
    if first == None:
        return first
    max_prev = q_prev = None
    max_val = q = first
    while q != None:
        if q.value > max_val.value:
            max_prev, max_val = q_prev, q
        q_prev = q
        q = q.next

    if max_prev == None:
        return first.next, max_val.value

    if max_val.next is None:
        max_prev.next = None
    else:
        max_prev.next = max_val.next
    return first, max_val.value


def InsertSort(first):
    q = first
    i = 0
    while q != None:
        q = q.next
        i += 1

    if i <= 1: return first
    Sort_First = None
    for j in range(i):
        first, MaxVal = del_max(first)
        Sort_First = insert(Sort_First, MaxVal)

    return Sort_First


first = Node(1, Node(3, Node(200, Node(63, Node(73, Node(93, None))))))
printList(InsertSort(first))
