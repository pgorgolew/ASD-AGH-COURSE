def BubbleSort(tab):
    n = len(tab)
    for i in range(n-1):
        for j in range(n-(1+i)):
            if tab[j] > tab[j+1]:
                tab[j],tab[j+1] = tab[j+1], tab[j]

    return(tab)
#O(n^2)

def SelectionSort(tab):
    n = len(tab)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if tab[min_index] > tab[j]:
                min_index = j
        
        tab[min_index], tab[i] = tab[i], tab[min_index]
    
    return(tab)

def InsertionSort(tab):
    n = len(tab)
    for i in range(1,n): 
        index = i
        number = tab[index]
        while index > 0 and number < tab[index-1]:
            tab[index], tab[index-1] = tab[index-1], tab[index]
            index -= 1
        
    return(tab)
