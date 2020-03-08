from turtle import Turtle, Screen


def hilbert_curve(turtle, direction, size, level):
    """
    funkcja rysująca krzywą hilberta dla określonego poziomu
    :param turtle: rodzaj żółwia
    :param direction: 1, jeśli chcemy iść w górę, -1, gdy idziemy w dół
    :param size: rozmiar rysunku
    :param level: stopień krzywej
    :return:
    """
    # przypadek bazowy
    if level < 1:
        return

    # rekurencyjne działanie
    turtle.left(direction * 90)
    hilbert_curve(turtle, - direction, size, level - 1)
    turtle.forward(size)
    turtle.right(direction * 90)
    hilbert_curve(turtle, direction, size, level - 1)
    turtle.forward(size)
    hilbert_curve(turtle, direction, size, level - 1)
    turtle.right(direction * 90)
    turtle.forward(size)
    hilbert_curve(turtle, - direction, size, level - 1)
    turtle.left(direction * 90)
    return


if __name__ == "__main__":

    screen = Screen()
    David = Turtle()

    animate = True  # można zmienić na true jeżeli nie chcemy oglądać animacji

    if animate:
        David.speed('fastest')
    else:
        screen.tracer(False)

    hilbert_curve(David, 1, 5, 5)

    screen.exitonclick()
