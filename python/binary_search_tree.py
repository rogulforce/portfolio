class TreeNode:    # węzeł drzewa (w tym korzeń lub liść)
    def __init__(self, key, value, left=None, right=None, parent=None):
        # TreeNode(5,"Piotr")
        self.key = key    # klucz po którym wstawiamy do drzewa
        self.payload = [value]    # zawartość węzła
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.quantity = 1   # nakładanie się węzłów

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        # sprawdza czy jest lewym dzieckiem
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        # sprawdza czy jest prawym dzieckiem
        return self.parent and self.parent.right_child == self

    def is_root(self):
        # korzeń: brak rodzica
        return not self.parent

    def is_leaf(self):
        # liść: brak dzieci
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_data(self, key, value, left_child, right_child):
        # zmiana danych węzła
        self.key = key
        self.payload = value
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def is_single(self):    # sprawdzamy czy jest więcej niż 1 wartość na węźle
        return len(self.payload) is 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)    # _put działa lepiej
        else:
            # gdy jest to pierwszy element
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        # działamy rekurencyjnie
        if key == current_node.key:    # zwiększamy ilość na tym węźle
            current_node.quantity = current_node.quantity + 1    # zwiększamy ilość
            current_node.payload.append(val)    # dodajemy zawartość na węźle
        elif key < current_node.key:    # mniejsze idą na lewo
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:   # większe idą na prawo
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):    # overloading of [] operator
        self.put(key, value)

    def get(self, key):
        if self.root:    # zaczynamy szukać od korzenia
            node = self._get(key, self.root)
            if node:
                return node.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:    # przypadek bazowy
            return None
        elif current_node.key == key:
            return current_node
        # działamy rekurencyjnie
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):    # overloading of [] operator
        return self.get(key)

    def __contains__(self, key):    # overloading of in operator
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size == 1 and self.root.key == key:    # tylko 1 węzeł
                self.root = None
                self.size = 0
        elif self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def find_successor(self, current_node):
        successor = self.find_min(current_node.right_child)
        return successor

    def find_min(self, current_node):
        current = current_node
        while current.has_left_child():    # "najbardziej lewe" drzewo
            current = current.left_child
        return current

    def place_swap(self, current_node, successor):
        # następca może jedynie być lewym liściem, bądź mieć prawe dziecko
        self.delete(successor.key)
        # dane liścia cały czas są przechowywane
        current_node.key = successor.key
        current_node.payload = successor.payload

    def remove(self, current_node):
        if not current_node.is_single():    # zabieramy jedną z wartości węzła
            current_node.payload.pop()
        else:
            if current_node.is_leaf():    # przypadek dla liścia
                if current_node.is_left_child():
                    current_node.parent.left_child = None
                else:
                    current_node.parent.right_child = None

            elif current_node.has_both_children():  # przypadek dla dwójki dzieci
                successor = self.find_successor(current_node)
                self.place_swap(current_node, successor)

            else:    # ma jedno dziecko
                if current_node.has_left_child():    # ma tylko lewe dziecko
                    if current_node.is_root:    # zamiana korzenia na jego lewe dziecko
                        current_node.replace_data(current_node.left_child.key, current_node.left_child.payload,
                                                  current_node.left_child.left_child,
                                                  current_node.left_child.right_child)
                    else:
                        current_node.left_child.parent = current_node.parent
                        if current_node.is_left_child():
                            current_node.parent.left_child = current_node.left_child
                        elif current_node.is_right_child():
                            current_node.parent.right_child = current_node.left_child

                else:    # ma tylko prawe dziecko
                    if current_node.is_root:    # zamiana korzenia na jego prawe dziecko
                        current_node.replace_data(current_node.right_child.key, current_node.right_child.payload,
                                                  current_node.right_child.left_child,
                                                  current_node.right_child.right_child)
                    else:
                        current_node.right_child.parent = current_node.parent
                        if current_node.is_left_child():
                            current_node.parent.left_child = current_node.right_child
                        elif current_node.is_right_child():
                            current_node.parent.right_child = current_node.right_child


if __name__ == "__main__":
    k = input("1 - usuwanie węzła z 2 dziećmi\n2 - usuwanie węzła z 1 dzieckiem\n3 - usuwanie liścia\n"
              "4 - usuwanie węzła z wieloma wartościami\n5 - usuwanie korzenia z dwoma odnogami\ninput: ")
    if k == "1":    # usuwanie korzenia z 2 dziećmi
        drzewo = BinarySearchTree()
        drzewo[20] = "A"
        drzewo[15] = "B"
        drzewo[16] = "H"
        drzewo[14] = "I"
        print(f'przed usunięciem: {drzewo.get(15)}')
        drzewo.delete(15)
        print(f'po usunięciu: {drzewo.get(15)}')
    elif k == "2":  # usuwanie węzła z 1 dzieckiem\
        drzewo = BinarySearchTree()
        drzewo[20] = "A"
        drzewo[15] = "B"
        drzewo[25] = "C"
        drzewo.put(22, "D")
        drzewo[21] = "E"
        print(f'przed usunięciem: {drzewo.get(25)}')
        drzewo.delete(25)
        print(f'po usunięciu: {drzewo.get(25)}')
    elif k == "3":    # usuwanie liścia
        drzewo = BinarySearchTree()
        drzewo[20] = "A"
        drzewo[15] = "B"
        drzewo[25] = "C"
        drzewo.put(22, "D")
        drzewo[21] = "E"
        print(f'przed usunięciem: {drzewo.get(21)}')
        drzewo.delete(21)
        print(f'po usunięciu: {drzewo.get(21)}')
    elif k == "4":  # usuwanie węzła z wieloma wartościami
        drzewo = BinarySearchTree()
        drzewo[20] = "A"
        drzewo[15] = "B"
        drzewo[25] = "C"
        drzewo.put(22, "D")
        drzewo[21] = "E"
        drzewo[25] = "C2"
        drzewo[25] = "C3"
        drzewo[25] = "C4"
        print(f'przed usunięciem: {drzewo.get(25)}')
        drzewo.delete(25)
        drzewo.delete(25)
        print(f'po usunięciu: {drzewo.get(25)}')
    else:   # usuwanie korzenia z dwoma odnogami
        drzewo = BinarySearchTree()
        drzewo[20] = "A"
        drzewo[15] = "B"
        drzewo[25] = "C"
        drzewo.put(22, "D")
        drzewo[21] = "E"
        drzewo[25] = "C2"
        drzewo[25] = "C3"
        drzewo[25] = "C4"
        drzewo[16] = "H"
        drzewo[14] = "I"
        print(f'przed usunięciem: {drzewo.get(20)}')
        drzewo.delete(20)
        print(f'po usunięciu: {drzewo.get(20)}')
        print(f'nowy korzeń: {drzewo.root.key}')
