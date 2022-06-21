from random import randint

def findMostCommon(word,k):
    n = len(word)
    if k>n: return 0
    if k==n: return 1

    substrings = [word[i:i+k] for i in range(n-k+1)]
    
    substrings = threeWayQuicksort(substrings,0,n-k)

    tmp = mostCommon = [substrings[0],0]
    
    for sub in substrings:
        if sub == mostCommon[0]:
            tmp[1] += 1
        else:
            if mostCommon[1] < tmp[1]:
                mostCommon = tmp
            
            tmp = [sub, 1]

    print(mostCommon[0])  
    


def threeWayPartition(T,l,r): #3 groupy [<,=,>] z random pivot
    if l>=r: return

    d = randint(l,r)
    T[l], T[d] = T[d], T[l] #Nasz pivot jest na początku, oraz jest randomowy
    x = T[l]
    ll = l
    i = l+1 #i to iterator, l to id dla nastepnego elementu < od pivota
    rl = r
    while i<=rl:
        if x > T[i]:
            T[ll], T[i] = T[i], T[ll]
            i+=1
            ll+=1
        elif x == T[i]: i+=1 
        else:
            T[i], T[rl] = T[rl], T[i]
            rl-=1

    return ll-1,rl+1

def threeWayQuicksort(T,l,r):
    while l<r:
        left,right = threeWayPartition(T,l,r) #left - koniec lewej czesci, right - poczatek prawej
        if left - l < r - right:  #Chcemy sortować mniejsze czesci, gwarantujemy logn pamieci (aktualne wywołania rekursji)
            threeWayQuicksort(T,l,left)
            l = right
        else:
            threeWayQuicksort(T,right,r)
            r = left

    return T

print(findMostCommon("ababaaaaabb", 3))