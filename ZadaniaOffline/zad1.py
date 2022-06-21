from random import randint, seed

def mergesort(T):
  def Divide(left,right):
    if right-left<=1:
      if T[left] > T[right]:
        T[left],T[right] = T[right], T[left]
      return
    else:
      middle = (left+right)//2
      Divide(left,middle)
      Divide(middle+1,right)
      TwoArraysToOne(left,middle,right)

  def TwoArraysToOne(left,middle,right):
    if T[middle] <= T[middle+1]: return #Połączenie "podtablic" daje nam posortowana tablice
    #Tworzymy tablice z dwoch posortowanych "podtablic tablicy T"
    #Nastepnie zamieniamy wartosci od T[left] do T[right], tak aby byly posortowane 
    n=right-left+1
    tab = [T[i] for i in range(left,right+1)]
    l1,r1=0,middle-left
    l2,r2=r1+1,n-1
    for i in range(n):
      if l2>r2 or (l1 <= r1 and tab[l1] < tab[l2]):
        T[left+i] = tab[l1]
        l1+=1
      else:
        T[left+i] = tab[l2]
        l2+=1
    
  
  if len(T) < 2: return T #Nic do sortowania

  left = 0
  right = len(T)-1
  middle = (left+right)//2
  Divide(left,right)
  return T
  
  
seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)
for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")


#Brzydki, w folderze algorytmy jest MERGE ktory korzysta
#tylko z jednej dodatkowej tablicy