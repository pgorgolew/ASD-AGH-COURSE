from zad3testy import runtests

def longest_incomplete(T,k):
    n = len(T)

    count = [0 for _ in range(k)]    
    uniq = [None for _ in range(k)]
    z = 1
    uniq[0] = T[0]
    i = 1
    while z < k:
        flag = False
        for j in range(z):
            if T[i] == uniq[j]: 
                flag = True
                break
        
        if not flag:
            uniq = insert(uniq,z,T[i])
            z+=1

        i+=1
    
    start = 0
    maxSequence = tmp = 0
    d = 0
    for i in range(n):
        num = T[i]
        uniqID = binaryLook(uniq,num)
        count[uniqID] += 1
        if count[uniqID] == 1:
            d+=1
        tmp += 1
        if d == k:
            maxSequence = max(maxSequence,tmp-1)
            for j in range(start,i+1):
                num2 = T[j]
                uniqID2 = binaryLook(uniq,num2)
                count[uniqID2] -= 1
                tmp -= 1
                if count[uniqID2] == 0:
                    d-=1
                    start = j+1
                    break
    
    return max(maxSequence,tmp)
            

def insert(uniq,z,num):
    uniq[z] = num
    for i in range(z-1,-1,-1):
        if num < uniq[i]:
            uniq[i+1], uniq[i] = uniq[i], uniq[i+1]
        else: break
    
    return uniq

def binaryLook(tab, x):
    n = len(tab)
    left = 0
    right = n-1
    middle = (left + right)//2
    while left < right:
        if tab[middle] == x: break

        if tab[middle] > x:
            right = middle-1
        else:
            left=  middle+1
        middle = (left + right)//2
    
    
    if tab[middle] != x: return False
    
    return middle


runtests( longest_incomplete ) 