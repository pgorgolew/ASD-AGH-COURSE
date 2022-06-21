from random import randint, shuffle, seed
# Rozwiązanie, zależy od problemu. Dla dużych tablic [np 1mln] o małej różnorodności elementów [np 0-100]
# przedstawiony poniżej sposób (3-partition(>,=,<)) jest wymagany - w innym razie Recurssion Error.
# W innych przypadkach mozna spokojnie uzywac zwykle partition.

def magicFive(A,l,p):
  n = p-l+1 #ilosc elementow
  if n < 15: #Gdy grup pelnych jest mniej niz 3, quickselect
    quickselect(A,(l+p)//2,l,p)
    return (l+p)//2
  z = n//5 #Dla ułatwienia, nie biorę pod uwagę ostatniej grupy (gdy jest niepełna)
  
  k=l
  for i in range(z):
    l2 = l + 5*i #początek grupy
    p2 = l2 + 4 #koniec grupy
    InsertionSort(A,l2,p2) 
    A[k],A[p2-2] = A[p2-2], A[k] #ustawiamy mediany na pozycje od l do l+z-1
    k+=1

  return magicFive(A,l,k-1) #wywołujemy rekurencyjnie na medianach

def quickselect(tab,k,l,p):
  d = randint(l, p) #randomowy pivot
  tab[d], tab[l] = tab[l], tab[d]
  left, right = ThreeWayPartition(tab,l,p) #równe elementy od left do right włącznie
  if k < left: return quickselect(tab,k,l,left-1)
  elif k > right: return quickselect(tab,k,right+1,p)
  else: return tab[left]

def ThreeWayPartition(T,l,r):
  x = T[l] #pivot to pierwszy element
  ll = l #wskazuje pierwszy element == x, jest indeksem dla kolejnego elementu < x
  i = l+1 #i to iterator, przeglądamy tablice od początku
  rl = r #wskazuje na indeks, do ktorego powinien trafic el > x
  while i<=rl:
      if x > T[i]:
          T[ll], T[i] = T[i], T[ll]
          i+=1
          ll+=1
      elif x == T[i]: i+=1 
      else:
          T[i], T[rl] = T[rl], T[i]
          rl-=1
  
  # ll wskazuje na indeks pierwszego elementu == x
  # rl wskazuje na indeks ostatniego elementu == x
  return ll,rl

def InsertionSort(A,l,p):
    for i in range(l+1,p+1):
      index = i
      while index > l and A[index] < A[index-1]:
        A[index],A[index-1]=A[index-1], A[index]
        index -= 1

def linearselect( A, k, l=0, p = None):
  #Mozna dołożyć warunek, że gdy szukamy k=0 albo k=len(A)-1
  #to robimy odpowiednio return min(A), return max(A)
  if p is None: p = len(A)-1
  piv_id = magicFive(A,l,p) 
  A[piv_id], A[l] = A[l], A[piv_id] #zamieniamy pivota z pierwszym elementem
  piv = A[l]
  left, right = ThreeWayPartition(A,l,p) #równe elementy od left do right włącznie
  if k < left: return linearselect(A,k,l,left-1)
  elif k > right: return linearselect(A,k,right+1,p)
  else: return A[left] #jezeli k jest pomiedzy left i right to mamy szukany element
