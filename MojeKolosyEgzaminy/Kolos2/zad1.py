from zad1testy import runtests
# f(i,w) - najwieksza ilosc studentow ktora moze zamieszkac w akademiku
#          rozwazajac budowe domow od 0 do i, ktorych koszt to w oraz lista akademikow do wybudowania

# f(i,w) = f(i-1,w) lub f(i-1,w-W[i]) + students[i]

#zlozonosc moze skoczyc do n^3
def select_buildings(T, p):
    n = len(T)

    students = [T[i][0] * (T[i][2]-T[i][1]) for i in range(n)] #liczba studentow na bundek
    F = [[-1 for _ in range(p+1)] for _ in range(n)]
    F[0][0] = (0,[])

    if T[0][3] <= p: F[0][T[0][3]] = students[0], [0]
        
    for i in range(1,n):
        for w in range(p+1):
            F[i][w] = F[i-1][w]
            
            if w < T[i][3] or F[i-1][w-T[i][3]] == -1: continue 

            if F[i-1][w-T[i][3]] != -1:
                f = True
                if F[i-1][w-T[i][3]] == -1: continue
                r = F[i-1][w-T[i][3]][1]
                ai,bi = T[i][1], T[i][2]
                for j in range(len(r)):
                    a1,b1 = T[r[j]][1], T[r[j]][2]

                    if ai > b1 or a1 > bi: continue #nie zawieraja sie

                    f = False
                
                if f == False: continue

                new = F[i-1][w-T[i][3]][0] + students[i]
                if F[i][w] == -1 or new > F[i][w][0]:
                    F[i][w] = (new, r+[i])

    res = F[n-1][1]
    w = 0
    for i in range(1,p+1):
        newRes = F[n-1][i]
        if newRes == -1: continue
        if res[0] < newRes[0]:
            res = newRes
            w = i
    
    j=0
    t=res[1]
    
    # nalezy jeszcze raz sprawdzic czy nie da sie czegos dolozyc -> niedokladna funkcja
    # dla ostatniego przykladu
    for i in range(n):
        if t[j]==i:
            j+=1
            continue

        if w+students[i] > p: continue

        ai,bi = T[i][1], T[i][2]
        f=True
        for k in range(len(t)):
            a1,b1 = T[t[k]][1], T[t[k]][2]

            if ai > b1 or a1 > bi: continue #nie zawieraja sie

            f = False

        if f==False: continue

        t = t[:j]+[i] + t[j:]

    return t

runtests( select_buildings ) 
