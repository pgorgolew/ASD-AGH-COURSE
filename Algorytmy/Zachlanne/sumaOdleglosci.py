# szukaj miejsca x w tablicy aby suma odleglosci do kazdego pkt byla min

# zadanie polega na tym zeby wybrac n//2 element
# dla ilosci elementow parzystych, musimy wziac srodkowy
# dla parzystych jakikolwiek punkt pomiedzy dwoma srodkowymi lub jeden z tych dwoch

def find(T):
    T = sorted(T)
    n = len(T)
    return T[n//2]
