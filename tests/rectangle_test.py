from figure.figs import Rectangle, Square, Triangle, Circle
from figure.figs import NotPositiveSideError
import pytest
import math


def test_check_name():
    fig = Rectangle(3, 4)
    assert fig.name == 'rectangle'


def test_check_angles():
    fig = Rectangle(3, 4)
    assert fig.angles == 4


@pytest.mark.parametrize(('a', 'b', 'ex'),
                         [(0, 1, 'одна из сторон не является положительным числом'),
                          (1, 0, 'одна из сторон не является положительным числом'),
                          (-1, 1, 'одна из сторон не является положительным числом'),
                          (1, -1, 'одна из сторон не является положительным числом'),
                          (1, 'skip', "__init__() missing 1 required positional argument: 'b'"),
                          ('skip', 'skip', "__init__() missing 1 required positional argument: 'b'")
                          ])
def test_exceptions(a, b, ex):
    Rectangle(1, 'a')
    try:
        if b == 'skip':
            Rectangle(a)
        elif a == 'skip':
            Rectangle()
        else:
            Rectangle(a, b)
    except TypeError as p:
        print(p)
        assert str(p) == ex
    except NotPositiveSideError as p:
        print(p.message)
        assert p.message == ex
    else:
        print('другой ексепшн?')
    finally:
        print('тест закончился')


@pytest.mark.parametrize(("a", "b", "area"), [(1, 2, 2),
                                              (3, 4, 12)
                                            ])
def test_area(a, b, area):
    fig = Rectangle(a, b)
    print(fig)
    print(fig.area())
    assert fig.area() == area


@pytest.mark.parametrize(("a", "b", "perimeter"),
                         [(1, 2, 6),
                          (3, 4, 14)
                          ])
def test_perimeter(a, b, perimeter):
    fig = Rectangle(a, b)
    assert fig.perimeter() == perimeter


@pytest.mark.parametrize(("a", "b", "new_fig", "new_area"),
                         [
                             (1, 2, Rectangle(1, 2), 4),
                             (3, 4, Square(1), 13),
                             (2, 3, Triangle(5, 3, 4), 12),
                             (10, 11, Circle(7), 110 + math.pi * 7**2),
                             (1, 1, 44, 'Ошибка. В метод передана не фигура')
                         ])
def test_add_area(a, b, new_fig, new_area):
    fig = Rectangle(a, b)
    add_a = fig.add_area(new_fig)
    assert add_a == new_area

