class QueueBaB:
    """
    Klasa implementująca kolejkę za pomocą pythonowej listy tak,
    że początek kolejki jest przechowywany na początku listy.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, *args):
        """
        Metoda służąca do dodawania obiektu do kolejki.
        Pobiera jako argument obiekty które mają być dodane.
        Niczego nie zwraca.
        """
        for item in args:
            self.items.insert(0, item)

    def dequeue(self):
        """
        Metoda służąca do ściągania obiektu do kolejki.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        deleted_item = self.items[-1]
        self.items.pop()
        return deleted_item

    def size(self):
        """
        Metoda służąca do określania wielkości kolejki.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w kolejce.
        """
        return len(self.items)

    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy kolejka jest pusta.
        Nie pobiera argumentów.
        Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
        """
        if self.size() == 0:
            return True
        else:
            return False


class QueueBaE:
    def __init__(self):
        self.items = []

    def enqueue(self, *args):
        """
        Metoda służąca do dodawania obiektu do kolejki.
        Pobiera jako argument obiekty które mają być dodane.
        Niczego nie zwraca.
        """
        for item in args:
            self.items.append(item)

    def dequeue(self):
        """
        Metoda służąca do ściągania obiektu do kolejki.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        deleted_item = self.items[0]
        self.items.pop(0)
        return deleted_item

    def size(self):
        """
        Metoda służąca do określania wielkości kolejki.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w kolejce.
        """
        return len(self.items)

    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy kolejka jest pusta.
        Nie pobiera argumentów.
        Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
        """
        if self.size() == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    bab = QueueBaB()
    bab.enqueue(1)
    bab.enqueue(2, 3)
    bab.enqueue(4)
    bab.enqueue(5, 6, 7, 8)
    bab.dequeue()
    bab.dequeue()
    print(f'size: {bab.size()}')
    print(f'items: {bab.items}')

    bae = QueueBaE()
    bae.enqueue(1)
    bae.enqueue(2, 3)
    bae.enqueue(4)
    bae.enqueue(5, 6, 7, 8)
    bae.dequeue()
    bae.dequeue()
    print(f'size: {bae.size()}')
    print(f'items: {bae.items}')

