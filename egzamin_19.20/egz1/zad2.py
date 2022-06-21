from zad2testy import runtests

#F[i][j] - (suma od i do j, optymalny wynik od i do j)
#F[i][i] = tab[i] (bo nic nie dodajemy)
#F[i][j] = F[i][z] + F[z][j] if min(abs(F[i][z]+F[z+1][j])) dla z {i,..,j-1}
def opt_sum(tab):
    def findbest(i,j,F):
        best = float("inf")
        ijsum = F[i][j-1][0] + F[j][j][0]
        for o in range(0,j-i):
            tmp = abs(ijsum)
            if tmp < F[i][i+o][1]: tmp = F[i][i+o][1]
            if tmp < F[i+o+1][j][1]: tmp = F[i+o+1][j][1]

            if tmp < best: best = tmp
        
        return (ijsum, best)

    n = len(tab)
    F = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        F[i][i] = (tab[i],0)
    
    for o in range(1,n): # o=j-i czyli o+1 to ilosc rozwazanych liczb
        for i in range(0,n-o):
            j = i+o
            F[i][j] = findbest(i,j,F)

    return F[0][n-1][1]

runtests( opt_sum )
