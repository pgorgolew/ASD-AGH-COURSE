from zad3testy import runtests
# Algorytm uzywa zmodyfikanej dijsktry ktora rozwaza dwa przypadki:
# a) mozemy isc o 1 abo o 2 (wczesniej szlismy o 1)
# b) mozemy isc tylko o 1 (wczesniej szliszmy o 2)
# jest to rozwazane dzieki tablicy d o wymiarach n na 2
# zlozonosc czasowa -> O(V^3), pamieciowa -> O(3*2*V) = O(V)
def jumper(G, s, w):
    def findMinimumVer(n,d,done):
        p = float("inf")
        i = None
        t=None
        for v in range(n):
            if not done[v][0] and d[v][0]< p:
                i = v
                t = 0
                p = d[v][0]
            if not done[v][1] and d[v][1]< p:
                i = v
                t = 1
                p = d[v][1]

        return i,t

    v,t = s,0
    n = len(G)
    d = [[float("inf"), float("inf")] for _ in range(n)]
    # d[v][0] -> mozemy isc o 1 oraz mozemy isc o 2
    # d[v][1] -> ostatnio szlismy o 2 wiec teraz musimy isc o 1
    done = [[False,False] for _ in range(n)]
    d[v] = [0, 0]
    while v != w:
        for i in range(n):
            if G[v][i] != 0:
                #zwykly krok dijsktry -> pozniej mozna o 1 lub o 2 wiec do done[i][0]
                if d[v][t] + G[v][i] < d[i][0] and not done[i][0]: 
                    d[i][0] = d[v][t]+G[v][i]

                if t == 0: #mozemy isc o dwa
                    for j in range(n):
                        if G[i][j] != 0 and not done[j][1] and\
                        d[j][1] > d[v][0] + max(G[v][i], G[i][j]):
                            d[j][1] = d[v][0] + max(G[v][i], G[i][j])          

        done[v][t] = True

        v, t = findMinimumVer(n,d,done)

    return d[v][t]

runtests(jumper)