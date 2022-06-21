def change(T,k):
    n = len(T)
    q = nwd(n,k)

    for j in range(q):
        index = j
        tmp = T[index]
        for i in range(n//q):
            newIndex = (index+k)%n
            tmp2 = T[newIndex]
            T[newIndex] = tmp
            index = newIndex
            tmp = tmp2

    return T

def nwd(x, y):
    while y != 0:
        y, x = x % y, y

    return x

tab = [1,2,3,4,5,6,7]
print(change(tab,11))