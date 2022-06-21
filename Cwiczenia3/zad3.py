import random
 
def partition(T, l, p):
    a=random.randint(l, p)
    pivot=T[a]
    T[a], T[p] = T[p], T[a]
    j=l
    for i in range(l, p):
        if(T[i]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j
 
def quicksort(T, l, p):
    if len(T)==0 or len(T)==1:
        return T
    stack=[0]*len(T)
    stack[0]=l
    stack[1]=p
    top=1
    while top>=0:
        p=stack[top]
        top-=1
        l=stack[top]
        top-=1
        q=partition(T, l, p)
        
        if q-1>l:
            top+=1
            stack[top]=l
            top+=1
            stack[top]=q-1

        if q+1 < p:
            top += 1
            stack[top]=q+1
            top += 1
            stack[top]=p


tab = [0,3,5,1,2,41,3,5,12,52,3,55,1,22]
quicksort(tab, 0, len(tab)-1)
print(tab)