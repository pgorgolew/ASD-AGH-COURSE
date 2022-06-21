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
    
print(binaryLook([0,1,2,3,5,6,12,15,16], 16))
