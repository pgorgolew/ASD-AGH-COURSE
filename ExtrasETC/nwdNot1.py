# Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n]. 
# Proszę napisać algorytm znajdujący rozmiar największego podzbioru liczb z A, takiego, że 
# ich GCD jest różny od 1. Algorytm powinien działać jak najszybciej.

#Tworzymy liste liczb pierwszych z zakresu <0,n>
#sprawdzamy ile liczb dzieli się przez daną liczbę pierwsza
#tam gdzie bedzie najwiecej to wielkosc najwiekszego podzbioru o nwd!=1

def first(a):
    if a == 2 or a ==3:
        return True
    elif a<=1 or a%2==0 or a%3==0:
        return False

    i = 5
    while i*i <= a:
        if a % (i) == 0 or a % (i+2) == 0:
            return False
        i +=6

    return True

def findAllFirsts(n):
    tab = []
    i = 2
    while n >= i:
        if first(i): tab += [i]
        i += 1

    return tab

def find(T):
    n = len(T)
    firsts = findAllFirsts(n)
    f = len(firsts)
    counts = [0]*f
    for x in T:
        for i in range(f):
            if x%firsts[i]==0: counts[i]+=1

    print("firsts:  ",firsts)
    print("counts:  ",counts)
    A = max(counts)
    return A

from random import randint
n=31
tab = [randint(0,n) for _ in range(n)]
print(tab)
print(find(tab))