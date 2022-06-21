#tab ma wspolrzedne podane jako (x1,y1,x2,y2) gdzie x1<x2,
#Sortujemy po  y1, i sprawdzamy do nastepnego y1

def DataChange(tab):
    for i in range(len(tab)):
        x1,y1,x2,y2=tab[i]
        width = x2 - x1
        Area = width * (y1-y2)
        tab[i]=[y2,y1,width,Area]
    
    return tab

def mergesort(tab,indeks): #zwraca posortowana tablice po y1 lub y2 (zalezy od zmiennej indeks)
    if len(tab) > 1:
        mid = len(tab)//2
        L = tab[:mid]
        R = tab[mid:]
        mergesort(L,indeks)
        mergesort(R,indeks)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][indeks] < R[j][indeks]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1
    
    return tab

def CountWater(WaterLevel,tab):
    AmountOfWater = 0
    for i in range(len(tab)):
        if WaterLevel >= tab[i][1]:
            AmountOfWater += tab[i][3] # +Area
        elif WaterLevel > tab[i][0]:
            AmountOfWater += (WaterLevel-tab[i][0])*tab[i][2]
    
    return AmountOfWater

def HowManyBoxes(tab,A):
    tab = DataChange(tab)
    tab = mergesort(tab,0) #sort po podstawie
    n=1
    while n<len(tab):
        WaterLevel = tab[n][0]
        AmountOfWater = CountWater(WaterLevel, tab)
        
        if AmountOfWater >= A: 
            count = 0
            for j in range(n):
                if tab[j][1] <= WaterLevel: count+=1
            if A==AmountOfWater:  return count #Jezeli ilosc wody sie zgadza
            #Jezeli sie nie zgadza, to podloga_wczesniejszego < waterlevel < podloga_aktualnego
            
            count2 = 0
            for k in range(n-1): #spr ile zalanych dla wczesniej "podłogi"
                if tab[k][1] <= tab[n-1][0]: count2+=1
            
            #Zmniejszenie poziomu wody do podstawy wczesniejszego pudełka, nie zmienia liczby zapełnionych pudełek
            if count==count2: return count 

            #Zmniejszenie poziomu wody sprawiło, że wypełniamy teraz o count-count2 mniej pudełek
            
            tab = mergesort(tab,1) #posortowana po y1, czyli "suficie"
            AmountOfWater = sum(box[3] for box in tab[:count2]) #sumujemy te pudełka, które na pewno będą "zalane"
            WaterToUse = A - AmountOfWater

            tab = tab[count2:] #Nasze spekulacje beda dotyczyc tylko tych "niewiadomych" pudełek

            for b in range(len(tab)-1,-1,-1): #sprawdzamy "od najwyzszego sufitu", czy ilosc wody starczy
                AmountOfWater = 0
                WaterLevel = tab[b][1]
                for i in range(len(tab)):
                    if i<=b: AmountOfWater += tab[i][3]
                    elif tab[i][0] < WaterLevel: AmountOfWater += tab[i][2]*(WaterLevel-tab[i][0])
                
                if AmountOfWater <= WaterToUse: return count2 + b + 1
            
            return count2

        n+=1

    #wyszlismy z while zatem wszystkie zalane lub trzeba rozważać od góry
    if sum(box[3] for box in tab) <= A: return len(tab) #-> WSZYSTKO ZALANE
    
    tab = mergesort(tab,1) #posortowana po y1, czyli "suficie"

    for b in range(len(tab)-2,-1,-1): #indeksy kolejnych pudełek od najwyższego sufitu, len-2 bo na pewno all nie  sa zalane
        WaterLevel = tab[b][1]
        AmountOfWater = 0
        for i in range(len(tab)):
            if i<=b: AmountOfWater += tab[i][3]
            elif tab[i][1] <= WaterLevel: AmountOfWater += tab[i][2]*(WaterLevel-tab[i][0])

        if AmountOfWater <= A: return b+1


rects = [(1, -1, 4, -2),
        (1, 3, 2, 1),
        (3, 5, 4, 1),
        (1, 5, 2, 4),
        (-4, 3, -1, 1)]

A = 16 #CHECK GRANICZNE
print(HowManyBoxes(rects,A))

"""A < 3 => 0
3 <= A < 13 => 1
13 <= A < 16 => 3
A >= 16 => 5"""

            

    
    
