def ile_cyfr(n):
    licznik = 0
    while n > 0:
        licznik += 1
        n //= 10

    return licznik


def first(a):
    if a == 2 or a == 3:
        return True
    elif a <= 1 or a % 2 == 0 or a % 3 == 0:
        return False

    i = 5
    while i * i <= a:
        if a % (i) == 0 or a % (i + 2) == 0:
            return False
        i += 6

    return True


def findAllFirsts(n):
    tab = []
    i = 2
    while n >= i:
        if first(i): tab += [i]
        i += 1

    return tab


def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10

    return suma


def rozklad_na_pierwsze(n):
    tab = []
    i = 2
    while n > 1:
        if n % i == 0:
            tab += [i]
            while n % i == 0:
                n //= i

        i += 1
    return tab


def wszystkie_dzielniki(n):
    tab = [1, n]
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            tab += [i]
            if i != int(n ** 0.5): tab += [n // i]
        i += 1

    return tab


def nwd(x, y):
    x, y = abs(x), abs(y)
    while y != 0:
        y, x = x % y, y

    return x


def nww(x, y):
    return (x // nwd(x, y)) * y


def czy_palindrom(t):  # dla tablicy lub stringu
    n = len(t)
    for i in range(n // 2):
        if t[i] != t[-(i + 1)]: return False

    return True


def czy_fib(wieksza, mniejsza):
    a = 1
    b = 1
    while a < mniejsza:
        b = b + a
        a = b - a
    if a == mniejsza and b == wieksza: return True
    return False


def sito(t):
    n = len(t)
    t_pom = [True for _ in range(n)]
    t_pom[0] = t_pom[1] = False
    x = 2
    while x <= n ** 0.5:
        if t_pom[x]:
            for i in range(x + x, n, x):
                t_pom[i] = False
        x += 1
