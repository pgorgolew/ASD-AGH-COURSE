# jedz do najdaleszej mozliwej stacji i tankuj na full
def minPetrols(L, t, S):
    n = len(S)
    k = 0  # aktualny kilometr
    i = 0  # aktualna stacja
    c = 0  # ilosc stacji
    while t > k + L:
        f = False
        while i < n and S[i] < k + L:
            i += 1
            f = True

        i -= 1
        if not f: return -1  # brak mozliwosci dojazdu

        k = S[i]
        c += 1

    return c


# minimalny koszt dotarcia do t gdy tankujemy ile chcemy
def minCost(L, t, S, P):
    n = len(S)
    k = 0  # aktualny kilometr
    i = -1  # iterator po stacjach
    c = 0  # koszt
    fuel = L  # aktualna ilosc paliwa
    while t > k + L:
        f = False

        currStation = i
        i += 1
        tmp = i  # najtansza stacja z dostepnych (na start nastepna)
        while i < n and S[i] < k + L:
            if P[i] < P[tmp]:
                tmp = i

            i += 1
            f = True

        if not f: return -1  # brak mozliwosci dojazdu

        if currStation != -1:
            if P[currStation] <= P[tmp]:  # jezeli aktualna stacja jest lepsza od reszty mozliwych
                c += P[currStation] * (L - fuel)  # tankuj full
                fuel = L - (S[tmp] - k)
            else:  # tankuj tyle zeby dojechac do najtanszej mozlwiej
                c += P[currStation] * (
                            S[tmp] - k - fuel)  # nie bedzie ujemne, bo gdyby mogl tam jechac od razu to by pojechal
                fuel = 0
        else:
            fuel = fuel - S[tmp] + k  # tyle stracilismy paliwa na dojazd do pierwszej wybranej stacji

        k = S[tmp]
        i = tmp

    if fuel < t - k:
        c += P[i] * (t - k - fuel)
    return c


# gdy trzeba tankowac wszedzie na full
# f(i) - min koszt dojechania do i oraz zatankowania full
# f(i) = min(f(i), f(s)+P[i]*(S[i]-S[s])) #s - stacje ktore maja w zasiegu i
def minCostFull(L, t, S, P):
    n = len(S)
    F = [float("inf") for _ in range(n)]
    if S[0] > L:
        return -1
    else:
        for i in range(n):
            if S[i] > L: break
            F[i] = P[i] * S[i]

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            road = S[i] - S[j]
            if road > L: break
            F[i] = min(F[i], F[j] + road * P[i])

    res = float("inf")
    for i in range(n - 1, -1, -1):
        if t - S[i] > L: break
        res = min(res, F[i])

    if res == float("inf"): return -1

    return res


L = 2
S = [1, 2, 3]
P = [0.8, 1, 0.8]
t = 4
print(minCostFull(L, t, S, P))
