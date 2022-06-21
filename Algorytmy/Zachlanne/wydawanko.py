# F[i] - minimalna ilosc monet do wydania kwoty i
def wydaj(M,s):
    F = [0 for _ in range(s+1)]
    for i in range(1,s+1):
        F[i] = float("inf")
        for j in M:
            if i-j >= 0: #ograniczenie, zeby nie wydac za duzo (czyli wyjsc poza tablice)
                F[i] = min(F[i], F[i-j]+1)
    return F[s]

M =[2,3,5]
s = 18
print(wydaj(M,s))

#O(s*len(M))
#sprawdzamy po kolei całą sumę