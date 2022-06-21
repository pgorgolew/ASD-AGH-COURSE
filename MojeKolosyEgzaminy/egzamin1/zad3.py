from zad3testy import runtests
# Pawel Gorgolewski
# Algorytm dynamiczny o funkcji:
# f(i,j) - optymalne rozwiazanie dla j przedzialow uzywajac i+1 pierwszych przedzialow a w tym i-tego
# f(i,j) = max(f(i-1,j), najwieksza czesc wspolna z i-tego i f(x,j-1), gdzie x to {k-1,k,...,i-1})
# w rozumieniu max mam namysli najwiekszy przedzial
#Zlozonosc to prawdopodobnie n^4, nie przechodzi dwoch ostatnich testow

def findBest(a,b): #znajduje wiekszy z dwoch przedzialow
  if a==None and b==None: return None
  
  if a==None: return b
  if b==None: return a

  tmp1 = a[1]-a[0]
  tmp2 = b[1]-b[0]

  if tmp1 > tmp2:
    return a
  else:
    return b

def connect(a,b):
  start = end = None
  if a==None or b==None: return None
  if a[0]>b[0]: start=a[0]
  else: start = b[0]

  if a[1]>b[1]: end = b[1]
  else: end = a[1]

  if start > end: return None
  else: return [start,end]

def kintersect( A, k ):
  def findBestWithJ(k,start,end):
    nonlocal A, f
    J = A[end+1] #dany przedzial
    res = None
    for i in range(start,end+1):
      res = findBest(res, connect(J,f[i][k]))
    
    return res
  
  n = len(A)
  f = [[None]*(k+1) for _ in range(n)]
  for i in range(n):
    f[i][1] = A[i]

  for j in range(2,k+1):
    for i in range(j-1, n):
      f[i][j] = findBestWithJ(j-1, j-2, i-1)

  best = f[k-1][k]
  for i in range(k,n):
    best = findBest(best, f[i][k])

  start,end = best[0], best[1]

  res=[]
  for i in range(n):
    if A[i][0] <= start and A[i][1] >= end:
      res.append(i)
  
  return res
  
runtests(kintersect)