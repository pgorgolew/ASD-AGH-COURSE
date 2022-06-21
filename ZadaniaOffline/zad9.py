from copy import deepcopy

# Alogrytm:
# 1) dla każdego wierzchołka wykonaj zmodyfikowany algorytm dijkstry, który zawiera dodatkowo najlepszy
#    cykl ktory znalezlismy do tej pory wraz z wierzcholkami ktore pomoga odtworzyc ten cykl poprzez 
#    usuniecie krawedzi miedzy nimi i znalezenie sciezki dijsktra (jest to zmienna best)
#   
#   zmodyfikowany algorytm dijsktry wykrywa cykl jezeli rozwaza krawedz do wierzcholka v, gdzie
#   prev[v] != None, czyli istnieje jakas inna sciezka od v do wierzcholka startowego
#   
#   Jest to poprawny sposob, poniewaz jezeli w danej iteracji zmienimy nasz best na cos, co nie jest cyklem, np 
#                                             /-- 4
#                                   1<-2<-3<-     |
#                                             \-- 5
#   sciezke od 4 do 1 oraz 5 do 1 wraz z krawedzia 4,5 to w kolejnych iteracjach na pewno zostanie to zamienione
#   na cykl 3,4,5 wiec program przez jakis czas moze przechowywac w zmiennej best, cos co nie stworzy nam cyklu
#   (takie sytuacje pojawiaja sie po zamiane prevow podczas trwania algorytmu dijsktry)
#
# 2) Po wykonaniu 1) best[0] zawiera wage cyklu, best[1] dwa wierzcholki [v,t] dzieki ktorym stworzymy cykl
#    a) usun krawedz {v,t} z grafu
#    b) znajdz najkrotsza sciezke z v,t (dijsktra)
#    c) stworz liste zawierajaca kolejne wierzcholki w cyklu
#    d) napraw graf -> dodaj z powrotem krawedz {v,t}

# Zlozonosc czasowa: O(V^2 * V + V^2) = O(V^3) [dla kazdego wierzcholka wykonaj dijsktre + na koniec jeszcze raz dijsktre]
# Zlozonosc pamieciowa O(3*V) = O(V) [listy: prev,done,d w algorytmie dijsktry]

def findMinimumVer(n,d,done):# O(V)
    p = float("inf")
    i = None
    for v in range(n):
        if not done[v]:
            if d[v] < p:
                i = v
                p = d[v]
    
    return i

def DijkstraBest(G,v,best): # O(V^2)
    n = len(G)
    d = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    done = [False for _ in range(n)]
    d[v] = 0
    while v != None:
        for i in range(n):
            if G[v][i] != -1 and not done[i]:

              ### modifikacja dijsktry poczatek
              if prev[i] != None:
                currWeight = d[i] + d[v] + G[v][i]

                if currWeight < best[0]:
                  best = (currWeight, [v,i])
              ### modifikacja dijsktry koniec

              if d[i] > d[v]+G[v][i]:
                d[i] = d[v]+G[v][i]
                prev[i] = v

        done[v] = True

        v = findMinimumVer(n,d,done)
    
    return best

def Dijkstra2(G,v,t): # O(V^2)
    n = len(G)
    d = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    done = [False for _ in range(n)]
    d[v] = 0
    while v != None:
        for i in range(n):
            if G[v][i] != -1 and not done[i] and d[v]+G[v][i] < d[i]:
                d[i] = d[v]+G[v][i]
                prev[i] = v

        done[v] = True

        v = findMinimumVer(n,d,done)

    return createPath(prev,t)
  
def createPath(prev,t): # O(V)
    #sciezka od wierzcholka startowego w Dijkstrze do t
    res = []
    if t == None: return res

    res = createPath(prev,prev[t])
    res.append(t)

    return res  

def min_cycle( G ):
    n = len(G)

    best = (float("inf"), [None,None])
    for i in range(n):
      best = DijkstraBest(G,i,best)
    
    # jezeli nasz best to nadal +inf to znaczy ze nie znalezlismy zadnego cyklu
    if best[0] == float("inf"): return []
    v,t = best[1]

    tmp = G[v][t]
    G[v][t], G[t][v] = -1, -1 #chwilowo usuwa krawedz {v,t}
    
    res = Dijkstra2(G,v,t)

    G[v][t], G[t][v] = tmp, tmp #naprawia graf
    return res

### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]  
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")
  
