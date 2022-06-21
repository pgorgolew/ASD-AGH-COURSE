from math import *

C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]

def createDistance(D,C,n):
  for i in range(n):
    for j in range(i+1,n):
      D[i][j] = sqrt(pow(C[i][2]-C[j][2],2) + pow(C[i][1]-C[j][1],2))
  
  return D

def funcArray(F,D,i,j):
  if F[i][j] != inf: return F[i][j]

  if i==j-1: #różnią się o jeden
    best = inf
    for k in range(j-1):
      best = min(best, funcArray(F,D,k,j-1) + D[k][j])
    F[i][j] = best

  else: #roznia sie o wiecej niz jeden
    F[i][j] = funcArray(F,D,i,j-1) + D[j-1][j]

  return F[i][j]
# zał S to miasto z najmniejszym x
# F[i][j] - min koszt sciezek od indeksu 0 do i oraz do j, (dla j>i>0), takich że
# łącznie każde miasto od 1 do j zostaje odwiedzone tylko raz
# D[i][k] odleglosc miasta o indeksie i do miasta o indeksie k
def bitonicTSP( C ):
  n = len(C)
  C = sorted(C, key = lambda x: x[1]) #sort po x
  D = [[0]*n for i in range(n)]
  D = createDistance(D,C,n)
  F = [[inf]*n for i in range(n)]

  F[0][0] = 0
  for i in range(1,n): #wypelniamy dystanse dla sciezek 0 oraz "i"
    F[0][i] = F[0][i-1] + D[i-1][i]
    
  best = inf
  for i in range(n-1):
    best = min(funcArray(F,D,i,n-1) + D[i][n-1], best)

  print(best)
  return best

  
bitonicTSP( C )

#Brak printowania drogi, nieskonczone zadanie offline