from figure.figs import Rectangle, Square, Triangle, Circle
from figure.figs import NotPositiveSideError
import pytest
import math


def test_check_name():
    """Проверка имени фигуры"""
    fig = Square(3)
    assert fig.name == 'square'


def test_check_angles():
    """Проверка кол-ва углов фигуры"""
    fig = Square(4)
    assert fig.angles == 4


@pytest.mark.parametrize(('a', 'ex'),
                         [(0, 'сторона не является положительным числом'),
                          (-1, 'сторона не является положительным числом'),
                          ('skip',  "__init__() missing 1 required positional argument: 'a'")
                          ])
def test_exceptions(a, ex):
    """Проверка возможных исключений при создании фигуры"""
    try:
        if a == 'skip':
            Square()
        else:
            Square(a)
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


@pytest.mark.parametrize(("a", "area"), [(1, 1), (7, 49)])
def test_area(a, area):
    """Проверка метода площади фигуры"""
    fig = Square(a)
    assert fig.area() == area


@pytest.mark.parametrize(("a", "perimeter"),
                         [(2, 8),
                          (9, 36)
                          ])
def test_perimeter(a, perimeter):
    """Проверка метода периметра фигуры"""
    fig = Square(a)
    assert fig.perimeter() == perimeter


@pytest.mark.parametrize(("a", "new_fig", "new_area"),
                         [
                             (1, Rectangle(1, 2), 3),
                             (3, Square(1), 10),
                             (2, Triangle(5, 3, 4), 10),
                             (10, Circle(7), 100 + math.pi * 7**2),
                             (1, 44, 'Ошибка. В метод передана не фигура')
                         ])
def test_add_area(a, new_fig, new_area):
    """Проверка метода добавления площади новой фигуры к площади текущей"""
    fig = Square(a)
    add_a = fig.add_area(new_fig)
    assert add_a == new_area
