# knapsack w O(n*sum(P)), gdzie P to tablica profitów

#F[i][p] - minimalna waga dla i-elementow chcac uzyskac profit p (lub wiekszy)
def knapsack(W,P,MaxW): #O(n*sum(P))
    n = len(W)
    sp = sum(P) 
    F = [[float('inf') for _ in range(sp+1)] for _ in range(n)] #O(n*sp)
    for i in range(n): F[i][0] = 0

    for p in range(1, P[0] + 1):
        F[0][p] = W[0]

    for i in range(1,n):
        for p in range(1, sp + 1):
            F[i][p] = F[i-1][p] #ustawiamy wage minimalna taka jak dla i-1 elementow

            # jezeli aktualnie rozwazany profit jest mniejszy badz rowny aktualnemu zyskowi z elementu,
            # bierzemy minimalną wartość z aktualnego F[i][p] oraz z wagi aktualnego elementu
            if p <= P[i]: F[i][p] = min(F[i][p], W[i]) 

            #jezeli aktualnie rozwazany profit jest wiekszy od aktualnego zysku z elementu, to
            #bierzemy min z aktualnej wagi + wage z profitu p-P[i] dla i-1 elementow oraz z aktualnej wartosci
            else: F[i][p] = min(F[i][p], F[i-1][p-P[i]] + W[i])
            
    for i in range(sp,-1,-1): #szukamy profitu dal ktorego waga bedzie przynajmniej rowna max val
        if F[n-1][i] <= MaxW:
            res = i
            break
    
    return res, F

def get_solution(F, W, P, i, p):
    if i == 0:
        if p == P[0]:
            return [P[0]]
        return []

    if p >= P[i] and (F[i][p] == F[i - 1][p - P[i]] + W[i]):
        return get_solution(F, W, P, i - 1, p - P[i]) + [P[i]]
    return get_solution(F, W, P, i - 1, p)

P = [10,8,4,5,3,7]
W = [4,5,12,9,1,13]
MaxW = 1

res, F = knapsack(W,P,MaxW)
print(res)
print(get_solution(F,W,P,len(P)-1,res))