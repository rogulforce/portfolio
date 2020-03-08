import re


class Stack:
    """
    prosta klasa stosu
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class TreeNode:    # węzeł drzewa (w tym korzeń lub liść)
    """
    klasa węzła
    hidden value - wartosc wezla i tego co pod nim sie znajduje
    der - pochodna wezla i tego co pod nia sie znajduje
    left - lewa odnoga, right - prawa
    drzewo buduje zawsze najpierw prawe dziecko

    w przypadku funkcji zlozonej ma jedynie prawe dziecko (czesto pojawia sie w 'if')
    """
    def __init__(self, value, hidden_value=None, der=None, left=None, right=None, parent=None):
        # TreeNode("+")
        self.payload = value    # zawartość węzła   (liczba / operator / funkcja)
        self.der = der    # pochodna węzła
        # wartosc wezla i tego co pod nim (zrobic cos z tym)
        self.hidden_value = hidden_value
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

    def replace_data(self, value, hidden_value=None, der=None, left=None, right=None):
        # zmiana danych węzła
        self.payload = value
        self.left_child = left
        self.right_child = right
        self.der = der
        self.hidden_value = hidden_value
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


class ParseTree:
    """
    klasa drzewa binarnego
    przyjmuje wyrazenie (niekoniecznie z nawiasami!!)
    """
    def __init__(self, expression, dx='x'):
        self.dx = dx    # po tym całkujemy
        self.root = TreeNode(expression)    # korzeń
        self.logarithms = []  # listy wziętych funkcji zlozonych
        self.sines = []    # sinusy
        self.cosines = []    # cosinusy
        self.exponents = []    # exp
        self.tans = []    # tangensy
        self.signs = ['*', '/', '+', '-']
        self.funs = ['L', 'S', 'C', 'E', 'T']
        self.digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, self.dx, 'm']

    def put(self, value, current_node, side='right'):
        # podrzucanie dziecka lewego bądź prawego, uzywane w self.auto_build
        if side == 'left':
            current_node.left_child = TreeNode(value, parent=current_node)
        else:
            current_node.right_child = TreeNode(value, parent=current_node)

    def auto_build(self, node):
        """
        rekurencyjna metoda budowania drzewa
        """
        self.complex_fun_sub(node)
        self.correction(node)

        if node.has_right_child():    # było budowane wcześniej
            return self.auto_build(node.right_child)
        elif node.has_left_child():
            return self.auto_build(node.left_child)
        else:    # jest liściem
            expression, left_kid, right_kid = self.split(node)
            # jesli da sie rozdzielić na a+b a*b a/b a-b
            if (left_kid is not None) and (right_kid is not None):
                node.payload = expression
                self.put(right_kid, node, 'right')
                self.put(left_kid, node, 'left')

                self.auto_build(node.right_child)
                self.auto_build(node.left_child)

            else:
                if node.payload in self.funs:    # dla L S C E T
                    self.complex_fun_developing(node)   # ściągamy z listy pobranych log,sin itd
                    self.auto_build(node.right_child)
                else:   # stała bądź x, bądź x^n
                    node.hidden_value = node.payload    # dodajemy hidden value dla liści
                    print(node.hidden_value)

    def complex_fun_sub(self, node):
        """"
        to jest potrzebne glownie przez idee dzialania programu niezaleznie od nawiasow, w metodzie correction
        zamieniamy + na )+( itd przy czym najpierw trzeba zabrac funkcje zlozone bo log(2+x) zamieniloby sie na
        log(2)+(x)
        """
        expression = node.payload

        self.logarithms.extend(re.findall(r'log\((.*?)\)', expression))
        for n in range(len(self.logarithms)):
            self.logarithms[n] = bracket_repair_for_complex_fun(self.logarithms[n])   # naprawiamy dla log(log(x)) itd
            expression = "L".join(expression.split(f'log({self.logarithms[n]})', 1))
        self.sines.extend(re.findall(r'sin\((.*?)\)', expression))
        for n in range(len(self.sines)):
            self.sines[n] = bracket_repair_for_complex_fun(self.sines[n])
            expression = "S".join(expression.split(f'sin({self.sines[n]})', 1))

        self.cosines.extend(re.findall(r'cos\((.*?)\)', expression))
        for n in range(len(self.cosines)):
            self.cosines[n] = bracket_repair_for_complex_fun(self.cosines[n])
            expression = "C".join(expression.split(f'cos({self.cosines[n]})', 1))

        self.exponents.extend(re.findall(r'exp\((.*?)\)', expression))
        self.exponents.extend(re.findall(r'e\^\((.*?)\)', expression))
        for n in range(len(self.exponents)):
            self.exponents[n] = bracket_repair_for_complex_fun(
                self.exponents[n])
            expression = expression.replace(f'exp({self.exponents[n]})', 'E').replace(f'e^({self.exponents[n]})', 'E')

        self.tans.extend(re.findall(r'tan\((.*?)\)', expression))
        for n in range(len(self.tans)):
            self.tans[n] = bracket_repair_for_complex_fun(self.tans[n])
            expression = "T".join(expression.split(f'tan({self.tans[n]})', 1))
        node.payload = expression

    def complex_fun_developing(self, node):
        # rozwija wczesniej zabrane funkcje
        if node.payload == 'L':
            node.payload = 'log'
            self.put(self.logarithms.pop(), node, 'right')
        elif node.payload == 'S':
            node.payload = 'sin'
            self.put(self.sines.pop(), node, 'right')
        elif node.payload == 'C':
            node.payload = 'cos'
            self.put(self.cosines.pop(), node, 'right')
        elif node.payload == 'E':
            node.payload = 'exp'
            self.put(self.exponents.pop(), node, 'right')
        elif node.payload == 'T':
            node.payload = 'tan'
            self.put(self.tans.pop(), node, 'right')

    def first_correction(self, node):  # pierwsza korekta (wykonywana tylko raz, pozniej osobno dla L,S,C,E)
        # pierwsze poprawki dla wyrazenia
        expression = node.payload
        expression = expression.replace(' ', '').replace(
            '**', '^').replace('ln', 'log')  # wywalamy spacje itd

        funs = ['log', 'sin', 'cos', 'exp', 'tan']
        for digit in self.digits:  # 2x -> 2*x ; 4( -> 4*( ; 3log -> 3*log
            expression = expression.replace(f'{digit}{self.dx}', f'{digit}*{self.dx}')\
                .replace(f'{digit}(', f'{digit}*(')
            for fun in funs:
                expression = expression.replace(f'{digit}{fun}', f'{digit}*{fun}')
        node.payload = expression

    def correction(self, node):  # po zamianie log na L
        # rozne takie .replace, staralismy sie zeby liczylo pochodną nawet jesli sie nie da nawiasow
        expression = node.payload
        expression = f'({expression})'
        expression = expression.replace(f'(-{self.dx}', f'(m1{self.dx}')
        expression = expression.replace('(-', '(m')
        for sign in self.signs:
            expression = expression.replace(f'{sign}', f'){sign}(')
        for digit in self.digits:  # 2x -> 2*x ; 4( -> 4*( ; 3log -> 3*log
            expression = expression.replace(f'{digit}{self.dx}', f'{digit})*({self.dx}')\
                .replace(f'{digit}(', f'{digit}*(')
            for fun in self.funs:
                expression = expression.replace(f'{digit}{fun}', f'{digit})*({fun}')
        node.payload = expression

    def split(self, node):  # tutaj parsujemy i rozdzielamy względem +-, pozniej */, pozniej
        """
        funkcja zwraca kolejno: zawartość węzła, lewego dziecka, prawego dziecka
        """
        expression = node.payload
        base = list(expression)
        openers_stack = Stack()
        # openers_stack.items = []
        signs = ['+', '-', '*', '/']
        sign_places = {}
        if [el for el in signs if el in base] != []:    # != zamiast 'is not' bo 'is not' nie działa
            # gdy wyrazenie zawiera +-/*
            for n in range(len(base)):
                element = base[n]
                if element is '(':
                    openers_stack.push(1)
                elif element is ')':
                    openers_stack.pop()
                else:
                    if not openers_stack.is_empty():  # gdy nie skończyły sie nawiasy
                        pass
                    else:   # zostaja same znaki +-*/
                        sign_places.update({element: base.index(element, n)})
                        # tym sposobem dostajemy *+-/ najbardziej na prawo
        if len(sign_places) == 0:  # expression = L,S,C,E, T, stała lub x
            if bracket_deleter(expression) == expression:
                node.payload = expression
                return expression, None, None
            else:    # gdy zamiast (x)+(2) jest ((x)+(2))
                # usuwamy zewnetrzna ramke i powtarzamy
                node.payload = bracket_deleter(expression)
                return self.split(node)
        else:    # gdy są * , / , + , -
            final_place = []
            for sign in signs[0:2]:    # dodajemy miejsca + i -
                if sign in sign_places:
                    final_place.append(sign_places[sign])
            if len(final_place) > 0:
                return expression[max(final_place)], expression[:max(final_place)], expression[max(final_place)+1:]
            else:
                for sign in signs[2:]:  # dodajemy miejsca * i /
                    if sign in sign_places:
                        final_place.append(sign_places[sign])
                return expression[max(final_place)], expression[:max(final_place)], expression[max(final_place) + 1:]

    def derivative(self, node):
        # tutaj liczymy sobie pochodną
        expression = node.payload
        expression = expression.replace('(', '').replace(')', '')
        if node.is_leaf():
            if self.dx not in expression:  # pochodna stałej
                node.der = '0'
                return
            else:
                if expression == self.dx:  # x
                    node.der = '1'
                    return
                elif '^' in expression:
                    if 'm' not in expression:
                        if expression[2:] != "2":
                            try:
                                node.der = f'{int(expression[2:])}*{self.dx}^{int(expression[2:])-1}'
                                return
                            except ValueError:
                                node.der = f'{float(expression[2:])}*{self.dx}^{float(expression[2:])-1}'
                                return
                        else:
                            node.der = f'2*{self.dx}'
                    else:
                        expression = expression.replace('m', '')
                        try:
                            node.der = f'm{int(expression[2:])}*{self.dx}^m{int(expression[2:])+1}'
                            return
                        except ValueError:
                            node.der = f'm{float(expression[2:])}*{self.dx}^m{float(expression[2:])+1}'
                            return
        elif node.has_both_children(): # dwojka dzieci to liczby pochodną każdego z nich
            self.derivative(node.right_child)
            self.derivative(node.left_child)
            if node.payload == '+':
                node.hidden_value = f'{node.left_child.hidden_value}+{node.right_child.hidden_value}'
                node.der = f'({node.left_child.der})+({node.right_child.der})'
            elif node.payload == '-':
                node.hidden_value = f'({node.left_child.hidden_value})-({node.right_child.hidden_value})'
                node.der = f'({node.left_child.der})-({node.right_child.der})'
            elif node.payload == '*':
                node.hidden_value = f'({node.left_child.hidden_value})*({node.right_child.hidden_value})'
                node.der = f'({node.left_child.der})*({node.right_child.hidden_value})+' \
                    f'({node.right_child.der})*({node.left_child.hidden_value})'
            elif node.payload == '/':
                node.hidden_value = f'({node.left_child.hidden_value})/({node.right_child.hidden_value})'
                node.der = f'(({node.left_child.der})*({node.right_child.hidden_value})-' \
                           f'({node.left_child.hidden_value})*({node.right_child.der}))/' \
                           f'(({node.right_child.hidden_value})*({node.right_child.hidden_value}))'
            return
        else:   # ma tylko prawe dziecko -> log, exp, cos, sin
            self.derivative(node.right_child)
            if node.payload == 'log':
                node.hidden_value = f'log({node.right_child.hidden_value})'
                node.der = f'({node.right_child.der})/({node.right_child.hidden_value})'
            elif node.payload == 'sin':
                node.hidden_value = f'sin({node.right_child.hidden_value})'
                node.der = f'({node.right_child.der})*(cos({node.right_child.hidden_value}))'
            elif node.payload == 'cos':
                node.hidden_value = f'cos({node.right_child.hidden_value})'
                node.der = f'(m1)*({node.right_child.der})*(sin({node.right_child.hidden_value}))'
            elif node.payload == 'exp':
                node.hidden_value = f'exp({node.right_child.hidden_value})'
                node.der = f'({node.right_child.der})*(exp({node.right_child.hidden_value}))'
            elif node.payload == 'tan':
                node.hidden_value = f'tan({node.right_child.hidden_value})'
                node.der = f'({node.right_child.der})/((cos({node.right_child.hidden_value})/' \
                           f'(cos({node.right_child.hidden_value}))))'
            return

    def tree_clear(self, node):
        """
        funkcja usuwająca 0 i podobne rzeczy z drzewa, czyści drzewo
        """
        if node.has_right_child():    # nie jest liściem
            self.tree_clear(node.right_child)
            if node.has_left_child():
                return self.tree_clear(node.left_child)
        else:   # dla liści
            if not node.is_root():
                if node.payload is '0':
                    if node.parent.payload == 'exp':    # exp(0) -> 1
                        node.parent.payload = '1'
                        node.parent.hidden_value = '1'
                        node.parent.right_child = None
                    elif node.parent.payload == 'log':
                        raise ValueError("can't count log(0)")
                    # sin(0) -> 0
                    elif node.parent.payload is 'sin' or node.parent.payload is '*':
                        node.parent.payload = '0'
                        node.parent.hidden_value = '0'
                        node.parent.right_child = None
                        node.parent.left_child = None
                        # usuwamy rekurencyjnie kolejne 0
                        return self.tree_clear(node.parent)
                    elif node.parent.payload is '/':
                        if node.parent.right_child == node:
                            raise ZeroDivisionError("can't devide by 0")
                        else:   # 0/n
                            node.parent.payload = '0'
                            node.parent.hidden_value = '0'
                            node.parent.right_child = None
                            node.parent.left_child = None
                            # usuwamy rekurencyjnie kolejne 0
                            return self.tree_clear(node.parent)
                    elif node.parent.payload is '+':    # zamienia + na węzeł niezerowego dziecka
                        if node.parent.right_child == node:
                            node.parent.replace_data(node.parent.left_child.payload,
                                                     hidden_value=node.parent.left_child.hidden_value,
                                                     left=node.parent.left_child.left_child,
                                                     right=node.parent.left_child.right_child)
                        else:
                            node.parent.replace_data(node.parent.right_child.payload,
                                                     hidden_value=node.parent.right_child.hidden_value,
                                                     left=node.parent.right_child.left_child,
                                                     right=node.parent.right_child.right_child)
                        # usuwamy rekurencyjnie kolejne 0
                        return self.tree_clear(node.parent)
                    elif node.parent.payload is '-':
                        if node.parent.right_child == node:
                            node.parent.replace_data(node.parent.left_child.payload,
                                                     hidden_value=node.parent.left_child.hidden_value,
                                                     left=node.parent.left_child.left_child,
                                                     right=node.parent.left_child.right_child)
                        else:
                            node.parent.replace_data(f'm{node.parent.right_child.payload}',
                                                     hidden_value=node.parent.right_child.hidden_value,
                                                     left=None, right=None)

                elif node.payload is "1":   # P/1 ---> P
                    if node.parent.payload is '/' and node.parent.right_child is node:
                        node.parent.replace_data(node.parent.left_child.payload,
                                                 hidden_value=node.parent.left_child.hidden_value,
                                                 left=node.parent.left_child.left_child,
                                                 right=node.parent.left_child.right_child)
                        return self.tree_clear(node.parent)
                    elif node.parent.payload is '*':
                        if node.parent.right_child == node:
                            node.parent.replace_data(node.parent.left_child.payload,
                                                     hidden_value=node.parent.left_child.hidden_value,
                                                     left=node.parent.left_child.left_child,
                                                     right=node.parent.left_child.right_child)
                        else:
                            node.parent.replace_data(node.parent.right_child.payload,
                                                     hidden_value=node.parent.right_child.hidden_value,
                                                     left=node.parent.right_child.left_child,
                                                     right=node.parent.right_child.right_child)


def bracket_repair_for_complex_fun(expression):
    # naprawia ramki, prosciej bylo tak niż z 're'
    diff = expression.count('(') - expression.count(')')
    if diff > 0:
        expression = f'{expression}{diff * ")"}'    # dodajemy koncowe nawiasy
    return expression


def bracket_deleter(expression):
    # usuwa zewnetrzne nawiasy przed policzeniem pochodnej
    if expression[0] == '(' and expression[-1] == ')':
        expression = expression[1:-1]
    return expression


def main(expression, dx='x', result='tree', degree=1):
    """
    glowna funkcja, liczy n-tą pochodną, domyslnie po x,
    jesli chce sie miec samą pochodną zamiast drzewa tej pochodnej,
    trzeba zmienic result='tree' na cos innego
    """
    tree = ParseTree(expression, dx)
    tree.first_correction(tree.root)
    tree.auto_build(tree.root)
    tree.tree_clear(tree.root)
    tree.derivative(tree.root)
    der = tree.root.der
    tree.root.hidden_value = tree.root.hidden_value.replace('m', '-')
    while degree > 0:
        tree2 = ParseTree(der, dx)
        tree2.first_correction(tree2.root)
        tree2.auto_build(tree2.root)
        tree2.tree_clear(tree2.root)
        tree2.derivative(tree2.root)
        tree2.root.hidden_value = tree2.root.hidden_value.replace('m', '-')
        degree -= 1
        der = tree2.root.der
    if result == 'tree':
        return tree2
    else:
        return tree2.root.hidden_value


if __name__ == "__main__":
    # '-' który nie jest operatorem zastąpiliśmy wewnątrz funkcji znakiem 'm'
    # example_1 = main('t*1*1/1/1 + sin(0)*2 - 0/3 + 123t^1234*0', dx='t')
    # print(f'derivative of   t*1*1/1/1 + sin(0)*2 - 0/3 + 123t^1234*0\n{example_1.root.hidden_value}\n')
    #
    # example_2 = main('tan(2y)', dx='y')
    # print(f'derivative of   tan(2y)\n{example_2.root.hidden_value}\n')
    #
    # example_3 = main('-t^(-3.5)', dx='t')
    # print(f'derivative of   -t^(-3.5)\n{example_3.root.hidden_value}\n')
    #
    # example_4 = main('e^(2x)+exp(8x^2)')
    # print(f'derivative of   e^(2x)+exp(8x^2)\n{example_4.root.hidden_value}\n')
    #
    # example_5 = main('log(log(x*y))', dx='y')
    # print(f'derivative of   log(log(x*y))\n{example_5.root.hidden_value}\n')
    #
    # example_6 = main('sin(sin(y))', dx='y')
    # print(f'derivative of   sin(sin(y))\n{example_6.root.hidden_value}\n')
    #
    # example_7 = main('-3/x')
    # print(f'derivative of   -3/x\n{example_7.root.hidden_value}\n')

    # example_8 = main('x^10', degree=7)
    # print(f'7th derivative of   x^10\n{example_8.root.hidden_value}\n')
    example = main('log(2/(x^2+1))')
    print(example.root.hidden_value)
