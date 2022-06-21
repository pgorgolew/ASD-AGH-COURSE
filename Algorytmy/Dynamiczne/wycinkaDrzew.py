# F[i] - najwiekszy zysk biorac pod uwage i pierwszych drzew
# bierzemy maxa z trzech sytuacji:
# 1) nie bierzemy itego elementu
# 2) bierzemy ity element oraz nie bierzemy i-1 elementu
# 3) bierzemy ity, i-1 a nie bierzemy i-2
# tutaj mozna dwa pod rząd, ale trzech nie
def treesOut(P):
    n = len(P)
    F = [0 for _ in range(n+1)]
    F[0],F[1],F[2] = 0, P[0], P[0] + P[1]

    for i in range(3,n+1): #i to kolejne drzewo (i-1 indeks w P)
        F[i] = max(F[i-1], F[i-2] + P[i-1], F[i-3] + P[i-1] + P[i-2])


    return F[n]

def treesOut2(P): #nie mozna dwoch pod rzad
    n = len(P)
    x2 = P[0] #dwa drzewa do tylu
    x1 = max(P[0], P[1]) # jedno drzewo do tylu
    for i in range(2,n):
        # najlepszy aktualny wynik to albo zostawiamy x1 albo do 2 drzewa do tylu dodajemu aktualne
        x1, x2 = max(x2+P[i], x1), x1
    
    return x1

P=[4,11,5,2,10]
print(treesOut2(P))