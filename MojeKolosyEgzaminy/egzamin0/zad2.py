from zad2testy import runtests
# self.X[i] - najlepszy wynik dla drzewa o i krawedziach
# Algorytm dziala dynamicznie, wypelnia tablice self.X zaczynajac od lisci
# wynik to max(self.X[k]) ze wszystkich nodów 
# (jezeli z jakiegos noda nie da sie to X[k]=None wiec nie bierzemy pod uwage)
# Zlozonosc czasowa O(n*k^2), pamieciowa O(n*k)
class Node:
  def __init__( self ):
    self.left    = None  # lewe podrzewo
    self.leftval = 0     # wartość krawędzi do lewego poddrzewa jeśli istnieje
    self.right   = None  # prawe poddrzewo
    self.rightval= 0     # wartość krawędzi do prawego poddrzewa jeśli istnieje
    self.X       = None  # miejsce na dodatkowe dane

def valuableTree( T, k ):
  def fillNodes(T):
    nonlocal best, k

    if T == None: return

    T.X = [None]*(k+1)
    T.X[0] = 0
    fillNodes(T.left)
    fillNodes(T.right)

    q = findBest(T)
    if best == None:
      best = q
    elif q != None:
      best = max(best, q)

  def findBest(T): #O(k^2)
    nonlocal k

    if T.left == None and T.right == None: return T.X[k]

    if T.left == None:
      for i in range(k-1,-1,-1):
        if T.right.X[i] != None:
          T.X[i+1] = T.right.X[i] + T.rightval
      T.X[1] = T.rightval
      return T.X[k]

    if T.right == None:
      for i in range(k-1,-1,-1):
        if T.left.X[i] != None:
          T.X[i+1] = T.left.X[i] + T.leftval
      T.X[1] = T.leftval
      return T.X[k]
    
    #mamy dwoje dzieci, trzeba sprawdzic wszystkie mozliwosci
    for i in range(1,k+1): 
      
      #tu rozwazamy sytuacje tylko left lub tylko right
      if i-1 > 0 and T.left.X[i-1] != None:
        if T.X[i] == None: 
          T.X[i] = T.leftval + T.left.X[i-1]
        else:
          T.X[i] = max(T.leftval + T.left.X[i-1], T.X[i])

      if i-1 > 0 and T.right.X[i-1] != None:
        if T.X[i] == None:
          T.X[i] = T.rightval + T.right.X[i-1]
        else:
          T.X[i] = max(T.X[i], T.rightval + T.right.X[i-1])

      #tu rozwazamy wszystkie sytuacje z leftval + rightval
      z = T.leftval + T.rightval
      for s in range(i-1):

        if i-2-s > 0 and T.left.X[i-2-s] == None: continue
        if s>0 and T.right.X[s] == None: continue

        if T.X[i]==None:
          T.X[i] = z+T.left.X[i-2-s]+T.right.X[s]
        else:
          T.X[i] = max(T.X[i], z+T.left.X[i-2-s]+T.right.X[s])
    
    return T.X[k]

  best = None
  fillNodes(T)

  return best
    
runtests( valuableTree )