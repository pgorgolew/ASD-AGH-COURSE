from random import randint

def SumSort(A,B,n):
    n2 = n**2
    sumTab = [0]*n
    for i in range(0,n2,n): #n*n(n razy liczymy sumy n-elemntowe)
        l = i
        p = i + n-1
        nSum = sum(A[j] for j in range(l,p+1))
        sumTab[i//n] = (nSum,l,p)
    
    sumTab = quicksort3(sumTab,0,n-1) #nlogn (bo jest)

    x = 0
    for i in range(n): #n*n (n razy przepisujemy n liczb)
        for j in range(sumTab[i][1],sumTab[i][2]+1): 
            B[x] = A[j]
            x+=1
    
    return B
    
def partition(T,l,r):
    x = T[r]
    i=l-1 #Bo na początku mamy 0 liczb <= x
    for j in range(l,r):
        if T[j] <= x:
            i+=1
            T[i],T[j] = T[j], T[i]
        
    T[i+1], T[r] = T[r], T[i+1]

    return i+1 

def randPartition(T,l,r):
    d = randint(l,r)
    T[r], T[d] = T[d], T[r] #Nasz pivot jest na początku, oraz jest randomowy
    return partition(T,l,r)   

def quicksort3(T,l,r): #teraz gwarantujemy logn zuzytej pamieci
    while l<r:
        q = randPartition(T,l,r)
        if q - l < r - q:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            quicksort3(T,l,q-1)
            l = q+1
        else:
            quicksort3(T,q+1,r)
            r = q-1
    return T

n = 100
n2 = n**2
T = [randint(0,2) for _ in range(n2)]
T2 = [0 for _ in range(n2)]
T2 = SumSort(T,T2,n)
Results = [0]*n
for i in range(0,n2,n):
    l = i
    p = i + n-1
    nSum = sum(T2[j] for j in range(l,p+1))
    sumID = i//n
    Results[sumID] = nSum
    if sumID!=0 and Results[sumID] < Results[sumID-1]:
        print("zle")
        break
    print(nSum)

#print(T2)