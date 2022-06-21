# Paweł Gorgolewski

from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 

# Zasada działania algorytmu:
# n-1 razy przeszukujemy k kolejnych nodow (jezeli istnieja) w celu znalezienia najmniejeszego noda z k-tych
# (jezeli n-1 bedzie dobry to n-ty tez musi byc, dlatego n-1 razy)
# po znalezieniu najmneijeszego z k-kolejnych noda, "wrzucamy" go na kolejne początkowe miejsce 
# (q jest ostatnim dobrze wybranym nodem, wiec kolejny bedzie za nim)

def SortH(p,k):
    war = Node()
    war.next = p
    q = prevp = war
    while p != None:
      minNode, prevMin = p, prevp
      z = 0
      while z < k and p.next != None: #patrzymy na kolejnych k nodow
        p,prevp = p.next, p
        if p.val < minNode.val:
          minNode, prevMin = p, prevp
        z+=1

      prevMin.next = minNode.next
      minNode.next = q.next
      q.next = minNode
      q = q.next
      prevp, p = q, q.next

    return war.next

runtests( SortH ) 


# złożoność czasowa O(k*n) -> n-1 razy szukamy najmnijeszego z k-kolejnych nodow
# złożonośc pamięciowa stała (oprocz podanych uzywamy takze 5 zmiennych i wartownika)
# dla k = 1 -> O(n) 
# dla k = logn -> O(nlogn)
# dla k = n -> O(n^2)