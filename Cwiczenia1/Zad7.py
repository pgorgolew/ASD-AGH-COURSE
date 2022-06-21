def search(tab,x):
    #zał ze posortowana niemalejąco
    n = len(tab)
    left = 0 #mniejsza
    right = n-1 #wieksza

    while left < right:
        tmp = tab[left] + tab[right]
        if tmp == x: return True
        elif tmp > x: right -=1
        else: left +=1
        
    return False
