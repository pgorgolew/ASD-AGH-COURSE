#F[i][j] - czy istnieje suma j dla i-pierwszych elementow

def subsetSum(A,s): # O(n*s), Pamięć O(n*s)
    n = len(A)
    F = [[False for _ in range(s+1)] for _ in range(n)]

    for i in range(n): F[i][0] = True #bo suma = 0 zawsze istnieje

    if A[0] < s: F[0][A[0]] = True
    if A[0] == s: return True

    for i in range(1, n): 
        k = 0

        while k <= s and k < A[i]: #przepisujemy to, czego i tak A[i] nie zmieni
            F[i][k] = F[i-1][k]
            k += 1

        while k <= s:
            F[i][k] = (F[i-1][k] or F[i-1][k-A[i]])
            k+=1
    
    printsolutions(F,A,s,n-1)
    return F[n-1][s]

def subsetSum2(A,s): # O(n*s), Pamięć O(s)
    n = len(A)
    F = [False for _ in range(s+1)]

    F[0] = True #bo suma = 0 zawsze istnieje

    if A[0] < s: F[A[0]] = True
    if A[0] == s: return True

    for i in range(1, n): 
        k = 0
        while k + A[i] <= s:
            F[k+A[i]] = F[k] or F[k+A[i]]
            k+=1
        
    return F[s]

def printsolutions(F,A,s,maxID,tab=[]): #Dziala dla subsetSum, bo F jest 2D
    if s == 0:
        print(tab)
        return
    
    if s<0: return

    for i in range(maxID,-1,-1):
        if F[i][s]: printsolutions(F,A,s-A[i], i-1, tab+[A[i]])

    return

T = [3, 4,5,2,1]
s = 10
print(subsetSum(T,s))
