from random import randint, seed

class Node:
  def __init__(self):
    self.next = None
    self.value = None
    
def sort(LeftW,RightW=None):
  pivot = LeftW.next
  q = pivot.next
  prev = pw = pivot 
  #pw to pierwszy Node, pivot ostatni, których wartość == pivot.value
  #będą wartownikami dla nastepnych wywołań funkcji sort 
  while q != RightW: 
    if pivot.value > q.value: #wstawiamy q przed Lewego Wartownika
      prev.next = q.next
      q.next = LeftW.next
      LeftW.next = q
      q = prev.next

    elif pivot.value < q.value: #zostawiamy
      prev = q
      q = q.next

    else:   #wstawiamy q przed aktualnego pivota, zmieniamy pivota na pivot.next
      prev.next = q.next
      q.next = pivot.next
      pivot.next = q
      q = prev.next

      if prev == pivot: #q i prev wskazywałyby cały czas na te same Nody
        #przyklad:  X -> 4 -> 4 -> X, gdzie X to wartownicy,
        #pierwsza czwórka to prev i zarazem pivot, druga czwórka to q
        q = q.next
        prev = prev.next

      pivot = pivot.next

  if LeftW.next != pw and LeftW.next.next != pw:   
    sort(LeftW,pw)
  if pivot.next != RightW and pivot.next.next != RightW:
    sort(pivot,RightW)

  return LeftW.next



def qsort( L ):
  if L == None or L.next == None: 
    return L 

  LeftW = Node() #Wartownik
  LeftW.next = L 
  L = sort(LeftW)

  return L



def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

