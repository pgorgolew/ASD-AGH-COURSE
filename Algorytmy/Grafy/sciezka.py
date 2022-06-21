#f(v) - wartosc najlepszej sciezki zaczynajacej sie na v i kierujący sie w strone lisci
#f(v) = max(0,v.val, v.val + f(left), v.val + f(right))

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.f = 0

def sciezka(v:Node):
    def f(v: Node):
        nonlocal best
        if v == None: return 0
        L = f(v.left)
        R = f(v.right)
        v.f = max(0, v.val, v.val + L, v.val + R)
        best = max(best,v.val + L + R)
        return v.f

    best = 0
    f(v)
    return best

A = Node(10)        #           A 10
B = Node(4)         #         /      \
C = Node(-5)        #        B 4      C -5
D = Node(-7)        #        |       /   \
E = Node(6)         #        D -7   E 6   F 8
F = Node(8)         #
A.left = B
B.left = D
A.right = C
C.left = E
C.right = F

print(sciezka(A))