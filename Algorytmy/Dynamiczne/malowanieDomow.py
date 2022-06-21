# F[i,t] - najlepszy podzial dla i plotow i t-pracowanikow
# F[i,t] = min{F[o,t-1],sum(o+1 do i)} -> dzielmy na t-1 pracownikow i jednego pracownika

def malowanko(A,t):
    n = len(A)
    F = [[0]*(t+1) for _ in range(n)]
    s = 0
    for i in range(n): #wypelniamy dla jednego pracownika (suma do i)
        s+=A[i]
        F[i][1] = s

    for p in range(2,t+1): #p-pracownicy
        for i in range(p-1,n): #plotow musi byc minimum p (p-1 bo indeks p-1 to plot nr p)
            for k in range(i,p-2,-1): #bo p-1 pracownikow musi miec p-1 plotow 
                F[i][p] = max(min(F[k-1][p-1],sum([A[z] for z in range(k,i+1)])),F[i][p])

    for s in F:
        print(s)

    return F[n-1][t]

T=[2,8,5,5,4,3,1]
t = 3

print(malowanko(T,t))