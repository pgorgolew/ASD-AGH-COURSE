from copy import deepcopy
# Algorytm jest oparty na rozwiazaniu z wykladu
# O(n^2) poniewaz zaden wierzcholek nie bedzie porownywac sie z innym wiecej niz raz
# Dla grafu pelnego kazdy wierzcholek sprawdzi czy moze przejsc do innego tylko jeden raz -> O(n*(n-1))
# Uzylem iteracyjnej modyfikacji DFS'a aby nie przepelniac stosu dla duzych gestych grafow
# Algorytm modyfikuje macierz G, jednak pozniej naprawia ja przez co pozostaje nienaruszona

# 1) Tworzy liste sasiedztwa (edges) aby nie sprawdzac czy istnieje krawedz z danego wierzcholka w O(n) (uzywajac G)
# 2) upewnia sie, ze warunek na cykl eulera jest spelniony (parzyste stopnie wierzcholkow)
# 3) wykonuje zmodyfikowany DFS, w ktorym chcemy przejsc wszystkie krawedzie a nie wierzcholki
# 4) Gdy w danym wywolaniu DFS'a wierzcholek nie ma juz zadnej dostepnej krawedzi zostaje dodany do listy res (na koniec)
#    w ktorej bedziemy trzymac kolejne wierzcholki z cyklu eulera
# 5) Po wykonaniu DFS'a sprawdza czy edges[i] jest pusta dla kazdego wierzcholka i (czyli spr czy zostala jakas krawedz)
#    Jezele nie, to oznacza ze graf nie jest spojny i nie ma cyklu eulera (przyklad dwa osobne trojkaty/kwadraty etc)

def euler( G ):
  def dfs(u):
    nonlocal edges,G,res,stack

    stack.append(u)
    while stack:
      u = stack[-1] # sprawdzany wierzcholek to ostatni wrzucony na stos
      while edges[u]:
        x = edges[u].pop()
        # jezeli uzylismy juz krawedzi u-x, to patrzymy na innych sasiadow oraz
        # naprawiamy macierz G do stanu poczatkowego (kazda krawedz bedzie wywolana 2 razy)
        if G[u][x] == 0: 
          G[u][x] = 1
          G[x][u] = 1
          continue 

        # Oznacza krawedz u-x jako 0 w G, bo zostala wlasnie wykorzystana
        G[u][x] = 0
        G[x][u] = 0

        #dodaje wierzcholek x na stos i ustawia x jako nasz aktualny wierzcholek u
        stack.append(x)
        u = x 
      
      # wierzcholek "u" nie ma juz dostepnych sasiadow, zatem dodajemy go do listy wynikowej
      # oraz cofamy sie do poprzedniego wierzcholka (cofanie zapewnia 22 linia kodu)
      stack.pop()
      res.append(u) 

  n = len(G)

  edges = [[] for _ in range(n)] #lista sasiadow, gdzie edges[i] zawiera sasiadow i
  for j in range(n-1):
    for i in range(j+1,n):
      if G[i][j] == 1: 
        edges[j].append(i)
        edges[i].append(j)

  for e in edges:
    if len(e) % 2 == 1: return None #istnieje wierzcholek o stopienu nieparzystym -> nie ma cylku eulera
  
  stack = []
  res = []
  dfs(0) #DFS mozna rozpoczac w dowolnym wierzcholu, nie musi byc 0

  for e in edges:
    #jezeli graf posiada inne krawedzie do ktorych dfs nie doszedl -> jest niespojny i nie ma cylku eulera
    #przyklad: graf sklada sie z dwoch osobnych trojkatow
    if sum(e) != 0: return None 

  return res
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")