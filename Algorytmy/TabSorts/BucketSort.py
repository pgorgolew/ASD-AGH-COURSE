def BucketSort(T): 
    m=10 #dla m=10, przedizaly to <0,0.1>....<0.9,1>
    B = [[] for _ in range(m)]
    n = len(T)
    for i in range(n): #wrzucamy liczby do odpowiednich kubełków
        d = int(T[i] * m)
        B[d].append(T[i]) 

    for i in range(m): #sortuj kubełki
        B[i] = InsertionSort(B[i])

    k = 0
    for i in range(m):
        for b in B[i]:
            T[k] = b
            k += 1

    return T
    
def InsertionSort(tab):
    n = len(tab)
    for i in range(1,n): 
        index = i
        number = tab[index]
        while index > 0 and number < tab[index-1]:
            tab[index], tab[index-1] = tab[index-1], tab[index]
            index -= 1
        
    return(tab)


x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434,0.125123,0.99,0.512,0.68,0.5123] 
print("Sorted Array is")
print(BucketSort(x))