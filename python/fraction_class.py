def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def value_different_types(other_fraction):
    if isinstance(other_fraction, Fraction):
        value = other_fraction.getValue()
    else:
        value = other_fraction
    return value


def float_spread(number, choice):
    # funkcja zamieniająca int i float na ułamki
    decimal_places = str(number)[::-1].find('.')
    if decimal_places == -1:
        # dla int
        if choice == 'fraction':
            return Fraction(number, 1)
        else:
            return number, 1
    else:
        # dla float
        if choice == 'fraction':
            return Fraction(int(number * 10**decimal_places), 10 **
                            decimal_places)
        else:
            return int(number * 10**decimal_places), 10**decimal_places


def swap_float_int_to_fraction(suspect, choice):
    # zależenie od wyboru rozszerzy nam licznik i mianownik,
    # bądź stworzy nowy ułamek

    if isinstance(suspect, Fraction):
        return suspect
    elif isinstance(suspect, (int, float)):
        return float_spread(suspect, choice)
    else:
        raise TypeError('object type must be either float, int or Fraction')


class Fraction:

    def __init__(self, numerator=0, denominator=1):
        """
        1. sprawdzamy czy podane wartosci są liczbami
        2. zamieniamy floaty na ulamki i mnozymy pierwszy przez odwrotnosc
           drugiego
        3. skracamy przez gcd dwóch liczb
        """

        if int(denominator) == 0:
            raise ZeroDivisionError('denominator must be nonzero number')

        num = swap_float_int_to_fraction(numerator, 0)[0] * \
            swap_float_int_to_fraction(denominator, 0)[1]
        den = swap_float_int_to_fraction(numerator, 0)[1] * \
            swap_float_int_to_fraction(denominator, 0)[0]

        greatest_common_dividor = \
            gcd(int(num), int(den))

        self._den = den / greatest_common_dividor
        self._num = num / greatest_common_dividor

    def getValue(self):
        return self._num / self._den

    def getDen(self):
        return self._den

    def getNum(self):
        return self._num

    # Przeciążam operatory kolejno: <, <=, >, >=, ==, !=, +, -, *, /

    def __lt__(self, other):
        return self.getValue() < value_different_types(other)

    def __le__(self, other):
        return self.getValue() <= value_different_types(other)

    def __gt__(self, other):
        return self.getValue() > value_different_types(other)

    def __ge__(self, other):
        return self.getValue() >= value_different_types(other)

    def __eq__(self, other):
        return self.getValue() == value_different_types(other)

    def __nq__(self, other):
        return self.getValue() != value_different_types(other)

    def __add__(self, other):
        other = swap_float_int_to_fraction(other, 'fraction')
        res_num = self.getNum() * other.getDen() + \
            other.getNum() * self.getDen()
        res_den = self.getDen() * other.getDen()
        result = Fraction(res_num, res_den)
        return result

    def __sub__(self, other):
        other = swap_float_int_to_fraction(other, 'fraction')
        res_num = self.getNum() * other.getDen() - other.getNum() * \
            self.getDen()
        res_den = self.getDen() * other.getDen()
        result = Fraction(res_num, res_den)
        return result

    def __mul__(self, other):
        other = swap_float_int_to_fraction(other, 'fraction')
        res_num = self.getNum() * other.getNum()
        res_den = self.getDen() * other.getDen()
        result = Fraction(res_num, res_den)
        return result

    def __truediv__(self, other):
        other = swap_float_int_to_fraction(other, 'fraction')
        if other.getNum() == 0:
            raise ZeroDivisionError('division by zero')
        res_num = self.getNum() * other.getDen()
        res_den = self.getDen() * other.getNum()
        result = Fraction(res_num, res_den)
        return result
    ###

    # nie definiuję metody __str__,bo metoda repr działa zarówno z print(),
    # jak i nazwą zmiennej wpisanej w interaktywnej sesji

    def __repr__(self):
        # dla 0 i L całkowitych bierzemy licznik, w przeciwnych
        # wypadku licznik / mianownik
        if self.getNum() == 0 or self.getDen() == 1:
            return str(int(self.getNum()))
        else:
            return '{}/{}'.format(int(self.getNum()), int(self.getDen()))


if __name__ == "__main__":
    f1 = Fraction(60.0, 1.2)
    print(f1)
    f2 = Fraction(4.5, 6)
    print(f1 * 2.5)
    print(f1 * 2)
    print(f1 - 1.23)
    print(f1 + 3.3333)
    print(f1 / f2)
    print(f1 * f2)

    f4 = Fraction(0, 3)
    print(f4)

    # obsługa błędów
    f3 = Fraction(2, "5")
    print(f1 / 0)

    # print(f1 < "f2")
