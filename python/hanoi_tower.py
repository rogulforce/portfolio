
class Stack:
    """
    prosta klasa stosu
    """

    def __init__(self, name):
        self.items = []
        self.name = name

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def info(self):
        return '{}: {}'.format(self.name, self.items)


def printing(n, from_rod, aux_rod, to_rod):
    # nadpisuję tę zmienną kilkukrotnie, ponieważ gubi wartości
    info = [from_rod.info(), aux_rod.info(), to_rod.info()]
    info.sort()
    print(info)


def move(n, from_rod, aux_rod, to_rod):

    # przypadek bazowy
    if n == 1:
        # Move disk 1 from rod {from_rod.name} to rod {to_rod.name}
        to_rod.push(from_rod.pop())
        printing(n, from_rod, aux_rod, to_rod)
        return

    # rekurencja
    move(n-1, from_rod, to_rod, aux_rod)
    # Move disk {n} from rod {from_rod.name} to rod {to_rod.name}
    to_rod.push(from_rod.pop())
    printing(n, from_rod, aux_rod, to_rod)
    move(n-1, aux_rod, from_rod, to_rod)
    return


def hanoi_tower(n, from_rod, aux_rod, to_rod):
    """
    funkcja rozwiązująca rekurencyjnie zagadanie wieży hanoi,
    jako argumenty przyjmuje liczbę krążków
    """
    if n > 0 and round(n) is n:

        # nakładanie krążków na pierwszą kolumnę
        for k in range(n):
            from_rod.push(n-k)

        printing(n, from_rod, aux_rod, to_rod)
        print('kolejne etapy:')
        move(n, from_rod, aux_rod, to_rod)
        return
    else:
        print("bad data")
        return


if __name__ == "__main__":
    A = Stack("A")
    B = Stack("B")
    C = Stack("C")
    hanoi_tower(4, A, B, C)
