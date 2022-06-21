def szukaj(tab):
    n = len(tab)
    i = 2
    if(n>=2):
        if tab[0] > tab[1]:
            MIN_val = tab[1]
            MAX_val = tab[0]
        else:
            MIN_val = tab[0]
            MAX_val = tab[1]
        
        while i <= n-2:
            if tab[i] > tab[i+1]:
                if tab[i] > MAX_val:
                    MAX_val = tab[i]
                if tab[i+1] < MIN_val:
                    MIN_val = tab[i+1]

            else:
                if tab[i] < MIN_val:
                    MIN_val = tab[i]
                if tab[i+1] > MAX_val:
                    MAX_val = tab[i+1]
            
            i+=2
        
        if n%2 == 1:
            if tab[i] > MAX_val:
                MAX_val = tab[i]
            if tab[i] < MIN_val:
                MIN_val = tab[i]

    elif n == 1:
        MIN_val = MAX_val == tab[0]
    
    else: return None
    