# Igor Sitek
"""
Algorytm wygląda tak: Idąc od liści w stronę korzenia, wiemy, że minimalny koszt
umożliwienia pojedynczej drogi pomiędzy liściem a korzeniem na najniższym poziomie
(poziom wyżej od liścia) to właśnie wartość tego wierzchołka, który jest rodzicem liścia
Chodzi mi o coś takiego:
      |  - gdzieś tam korzeń
     (5)  - o tym najniższym poziomie mówię
   /    \
 (_)     (_) - liście
 Tutaj minimalny koszt na tym poziomie to 5.

 Następnie wynik ten na wyższych poziomach drzewa mogę ulepszyć, korzystając z funkcji:
 f(v) - minimalna suma uniemożliwiająca nieprzerwane scieżki z v traktowanego jako korzeń
        do wszystkich liści tego poddrzewa
 f(v) = min( f(u) + f(w), v.value), gdzie v - wierzchołek niebędący korzeniem całego drzewa,
                                    u, w - dzieci v
Edge cases:
f(liść) = infinity (nie ma takiego kosztu, żeby uniemożliwić tę ścieżkę)
Jeśli któregoś dziecka nie ma, to przyjmuję wartość f tej części jako 0
(nie muszę nic z tą częścią robić, bo nie ma tam liści)

Korzenia całego drzewa nie mogę usunąć, zatem wynik to f(u) + f(w), gdzie u,w - dzieci korzenia
# Obliczeniowa: O(|V|), bo do każdego wierzchołka wejdę tylko raz i sprawdzę f od jego dzieci
# Pamięciowa: O(1)
"""


from zad2testy import runtests
from math import inf

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(main_root):

    def rec(root):
        if root.left is None and root.right is None:
            return inf

        f_l = rec(root.left) if root.left is not None else 0
        f_r = rec(root.right) if root.right is not None else 0

        return min(f_l + f_r, root.value)

    left = rec(main_root.left) if main_root.left is not None else 0
    right = rec(main_root.right) if main_root.right is not None else 0
    return left + right

# no już widzę ten plagiacik za 13 linijek kodu :D
    
runtests(cutthetree)


