from zad2testy import runtests

def fast_list_prepend(L,a):
    aL = FastListNode(a)
    if L == None: return aL
    aL.next.append(L)
    q=L
    i=0
    while True:
      if len(q.next) < i+1: break
      aL.next.append(q.next[i])
      q = q.next[i]
      i+=1

    return aL


class FastListNode:
  def __init__(self, a):
    self.a = a     # przechowywana liczba calkowita
    self.next = [] # lista odnosnikow do innych elementow; poczatkowo pusta

  def __str__(self): # zwraca zawartosc wezla w postaci napisu
    res = 'a: ' + str(self.a) + '\t' + 'next keys: '
    res += str([n.a for n in self.next])
    return res




runtests( fast_list_prepend ) 
