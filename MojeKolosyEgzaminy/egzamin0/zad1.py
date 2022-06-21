from zad1testy import runtests
# ord('a') = 97 ord('z') = 122 -> 26 liter
# 1) przetwórz pierwsze słowo do tablicy letter
# 2) sprawdzaj czy kolejne litery z drugiego słowa spełniają założenia

# jezeli aktualnie pierwsza litera z tablicy letter nie spelnia zalozenia odleglosciowego
# to wiemy ze slowa nie sa anagramami (bo kolejna litera bedzie miala z nia jeszcze wieksza odleglosc)

# zlozonosc czasowa O(n)
def tanagram(x, y, t):
    letters = [[] for _ in range(26)]
    ind = [0 for _ in range(26)]
    n = len(x)

    for i in range(n):
        letters[ord(x[i])-97].append(i)
    
    for i in range(n):
        l = ord(y[i])-97
        
        # słowa różnią się pod względem liter
        if ind[l] == len(letters[l]):
            return False
        
        # jezeli nie mozna dopasowac aktualnej litery z najwczesniejsza
        if abs(i-letters[l][ind[l]]) > t:
            return False
        
        ind[l] += 1

    return True


runtests( tanagram )