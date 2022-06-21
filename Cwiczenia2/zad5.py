def lider_ciagu(T):
    def candidate(tab):
        maj_index = 0
        count = 1
        for i in range(1,len(tab)): 
            if tab[maj_index] == tab[i]: 
                count += 1
            else: 
                count -= 1
            if count == 0: 
                maj_index = i 
                count = 1

        return tab[maj_index] 
    
    def check(tab,number):
        k = 0
        for i in range(len(tab)):
            if number == tab[i]: k+=1
        if k > len(tab)//2: return True
        else: return False
        if len(T)==0: return False
    
    return check(T,candidate(T))
T=[6,6,6,6,6,3,3,3,3]
print(lider_ciagu(T))