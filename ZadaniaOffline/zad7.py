from queue import PriorityQueue

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]

class Node:
  def __init__(self, symbol, freq, left=None, right=None):
    self.symbol = symbol
    self.freq = freq
    self.left = left
    self.right = right
    self.code = ""

def heapify(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l].freq < T[m].freq: m = l
    if r < n and T[r].freq < T[m].freq: m = r
    if m != i:
        T[m], T[i] = T[i], T[m]
        heapify(T,n,m)

def HeapInsert(v,T,n): #wstaw na koniec, przesuwaj w gore gdy parent < val
    i = n-1
    T[i] = v
    while i > 0:
        p = parent(i)
        if T[i].freq <= T[p].freq:
            T[i], T[p] = T[p], T[i]
            i = p
        else: break
    
    return 

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

def buildHeap(T):
    n = len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,n,i)

def getMin(T,n): 
    v = T[0]
    T[n-1], T[0] = T[0], T[n-1]
    heapify(T,n-1,0)
    return v

def binaryLook(x, T):
    n = len(T)
    left = 0
    right = n-1
    middle = (left + right)//2
    while left < right:
        if T[middle].freq == x: break

        if T[middle].freq > x:
            right = middle-1
        else:
            left=  middle+1
        middle = (left + right)//2
    
    return middle

def huffman( S, F ):
  def createCodes(v, code=''):
    nonlocal q

    curr = code + str(v.code)
 
    if v.left is not None: createCodes(v.left, curr)
    if v.right is not None: createCodes(v.right, curr)
 
    if not v.left and not v.right:
      v.code = curr
      nodeTab[q] = v
      q+=1
    
  n = len(S)

  nodeTab = [Node(S[i],F[i]) for i in range(n)] #tworzymy tablice nodow

  buildHeap(nodeTab) #budujemy kopiec

  while n > 1:
    leftN = getMin(nodeTab, n)
    n -= 1
    rightN = getMin(nodeTab, n)

    leftN.code = 0
    rightN.code = 1

    newNode = Node(leftN.symbol + rightN.symbol, leftN.freq + rightN.freq, leftN, rightN)

    HeapInsert(newNode, nodeTab, n) #dodaj do tablicy noda stworzonego z dwóch o najmniejeszej freq

  #w nodeTab zostal 1 node, jest to korzeń drzewa
  q = 0
  root = nodeTab[0]
  createCodes(root)

  nodeTab = sorted(nodeTab, key = lambda x: x.freq)

  s = 0
  for i in range(q):
    v = binaryLook(F[i], nodeTab)
    s += nodeTab[v].freq * len(nodeTab[v].code)
    print(f"{nodeTab[v].symbol} : {nodeTab[v].code}")

  print(f"suma to {s}")

huffman( S, F )