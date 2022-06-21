#algorytm zachłanny, ustawia przedział jednostkowy na pierwszej możliwej liczbie z X
#posortuj 

def przedzialy(X):
    X = sorted(X)
    n = len(X)

    z = X[0] + 1 #zasieg ostatniego przedzialu
    c = 1 #licznik


    for i in range(1, n):
        if X[i] > z:
            c+=1
            z = X[i] + 1

    return c

X = [0.15,1.02,1.55,2.91]
print(przedzialy(X))
