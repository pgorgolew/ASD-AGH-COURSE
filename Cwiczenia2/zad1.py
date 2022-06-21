from time import time
from random import randint,seed

class Node:
    def __init__(self, value=None, next=None):
   	 self.value = value
   	 self.next = next
   	 
def printList(first):
    while first != None:
        print(first.value)
        first = first.next 

def merge(first1, first2):
    if first1 is None: return first2

    if first2 is None: return first1

    war = Node()
    q = war
    while first1 != None and first2 != None:
        if first1.value > first2.value:
            q.next = first2
            first2=first2.next
        else:
            q.next = first1
            first1 = first1.next
        
        q = q.next

    if first1 != None:
        q.next = first1
    else:
        q.next = first2

    return war.next        

def series(first):
    tab = []
    q = first
    while q != None:
        tab += [q]
        p = q
        while p.next != None and p.value <= p.next.value:
            p = p.next
        w = p.next
        p.next = None
        q = w
    
    #teraz mamy tablice rosnących list
    return tab

def ListMerge_N2(tab):
    n = len(tab)
    for i in range(n-1):
        tab[i+1] = merge(tab[i],tab[i+1])
    
    return tab[n-1]

def ListMerge_nlogn(tab):
    tmp = n = len(tab)
    if n == 1: return tab[0]
    elif n == 0: return None
    k=1
    MissedList = []
    LastIdMissed = False
    while True:
        if tmp%2 == 1:    #Zdarza sie, ze pomijamy list, dodajemy wiec je do osobnej tablicy (poza elementem na ostatnim ID)
            if LastIdMissed:
                MissedList += [tab[2*(tmp // 2 + 1)*k-1-k]]
            LastIdMissed = True

        tmp //= 2 #tyle scaleń jesteśmy w stanie zrobić
        for i in range(tmp):
            #scalamy dwie listy, wskaźnik na nową listę zapisujemy w tab na większym z indeksów wcześniejszych list
            tab[2*(i+1)*k-1] = merge(tab[2*(i+1)*k-1],tab[2*(i+1)*k-1-k]) 

        if tmp == 1:
            #wszystkie listy połączone, n to 2^x, x naturalny
            if n == k*2: break
            #n-1-(n%k) to indeks do tab zawierający wskaźnik na posortowaną listę, zawierającą wszystkie Nody z 
            #wcześniejszych list, należy użyć merge na niej oraz liście, której wskaźnik znajduje się na ostatnim (n-1)
            #indeksie tab, aby powstała posortowana lista, zawierająca wszystkie Nody z wszystkich list
            else:
                if MissedList == []:
                    if n == 3: tab[2] = merge(tab[2],tab[1])  #(n-1-n%k) nie działa dla k=1, a konczymy funkcje dla k=1 <=> n=3 xd
                    else: tab[n-1] = merge(tab[n-1],tab[n-1-(n%k)])
                    break
                MissedList += [tab[2*k-1]] #element na którym skonczył sie for loop, tmp było 1, i = 0
                MissedList += [tab[n-1]]

                return ListMerge_nlogn(MissedList)
        
        k*=2
    return tab[n-1]

seed(42)

f = w = Node(0)
for _ in range(2000):
    w.next=Node(randint(-100,100))
    w=w.next

#f = Node(1,Node(4,Node(3,Node(2,Node(9,Node(7,Node(2)))))))
print("==================")
start = time()
ListMerge_nlogn(series(f))
end = time()
print(end-start)
print("==================")
seed(42)
f = w = Node(0)
for _ in range(2000):
    w.next=Node(randint(-100,100))
    w=w.next
start = time()
ListMerge_N2(series(f))
end = time()
print(end-start)