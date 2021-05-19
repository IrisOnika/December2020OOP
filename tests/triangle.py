from figure.figs import Rectangle, Square, Triangle, Circle
from figure.figs import NotPositiveSideError, IncorrectTriangleSideError
import pytest
import math


def test_check_name():
    """Проверка имени фигуры"""
    fig = Triangle(3, 4, 5)
    assert fig.name == 'triangle'


def test_check_angles():
    """Проверка кол-ва углов фигуры"""
    fig = Triangle(4, 4, 3)
    assert fig.angles == 3


@pytest.mark.parametrize(('a', 'b', 'c', 'ex'),
                         [(0, 1, 1, 'одна из сторон треугольнака не является положительным числом'),
                          (1, 0, 1, 'одна из сторон треугольнака не является положительным числом'),
                          (1, 1, 0, 'одна из сторон треугольнака не является положительным числом'),
                          (-1, 1, 1, 'одна из сторон треугольнака не является положительным числом'),
                          (1, -1, 1, 'одна из сторон треугольнака не является положительным числом'),
                          (1, 1, -1, 'одна из сторон треугольнака не является положительным числом'),
                          (2, 2, 4, 'сумма двух сторон треугольника меньше третьей'),
                          (3, 12, 5, 'сумма двух сторон треугольника меньше третьей'),
                          (5, 2, 2, 'сумма двух сторон треугольника меньше третьей'),
                          (1, 1, 'skip', "__init__() missing 1 required positional argument: 'c'"),
                          (1, 'skip', 'skip', "__init__() missing 1 required positional argument: 'c'"),
                          ('skip', 'skip', 'skip', "__init__() missing 1 required positional argument: 'c'")
                          ])
def test_exceptions(a, b, c, ex):
    """Проверка возможных исключений при создании фигуры"""
    try:
        if c == 'skip':
            Triangle(a, b)
        elif b == 'skip':
            Triangle(a)
        elif a == 'skip':
            Triangle()
        else:
            Triangle(a, b, c)
    except TypeError as p:
        print(p)
        assert str(p) == ex
    except NotPositiveSideError as p:
        print(p.message)
        assert p.message == ex
    except IncorrectTriangleSideError as p:
        print(p)
        assert p.message == ex
    else:
        print('другой ексепшн?')
    finally:
        print('тест закончился')


@pytest.mark.parametrize(("a", "b", "c", "area"), [(11, 90, 97, 396), (3, 4, 5, 6)])
def test_area(a, b, c, area):
    """Проверка метода площади фигуры"""
    fig = Triangle(a, b, c)
    assert fig.area() == area


@pytest.mark.parametrize(("a", "b", "c", "perimeter"),
                         [(2, 4, 3, 9),
                          (9, 11, 7, 27)
                          ])
def test_perimeter(a, b, c, perimeter):
    """Проверка метода периметра фугуры"""
    fig = Triangle(a, b, c)
    assert fig.perimeter() == perimeter


@pytest.mark.parametrize(("a", "b", "c", "new_fig", "new_area"),
                         [
                             (17, 10, 9, Rectangle(1, 2), 38),
                             (8, 5, 5, Square(2), 16),
                             (13, 13, 10, Triangle(5, 3, 4), 66),
                             (13, 14, 15, Circle(7), 84 + math.pi * 7**2),
                             (1, 1, 1, 44, 'Ошибка. В метод передана не фигура')
                         ])
def test_add_area(a, b, c, new_fig, new_area):
    """Проверка метода добавления площади новой фигуры к площади текущей"""
    fig = Triangle(a, b, c)
    add_a = fig.add_area(new_fig)
    assert add_a == new_area
