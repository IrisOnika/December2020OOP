from figure.figs import Rectangle, Square, Triangle, Circle
from figure.figs import NotPositiveSideError
import pytest
import math


def test_check_name():
    """Проверка имени фигуры"""
    fig = Circle(3)
    assert fig.name == 'circle'


def test_check_angles():
    """Проверка кол-ва уголов фиругы"""
    fig = Circle(4)
    assert fig.angles == 0


@pytest.mark.parametrize(('a', 'ex'),
                         [(0, 'радиус не является положительным числом'),
                          (-1, 'радиус не является положительным числом'),
                          ('skip',  "__init__() missing 1 required positional argument: 'a'")
                          ])
def test_exceptions(a, ex):
    """Проверка возможных исключений при создании фигуры"""
    try:
        if a == 'skip':
            Circle()
        else:
            Circle(a)
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


@pytest.mark.parametrize(("a", "area"), [(1, math.pi), (9, 81 * math.pi)])
def test_area(a, area):
    """Проверка метода площади фигуры"""
    fig = Circle(a)
    assert fig.area() == area


@pytest.mark.parametrize(("a", "perimeter"),
                         [(3, 6 * math.pi),
                          (9, 18 * math.pi)
                          ])
def test_perimeter(a, perimeter):
    """Проверка метода периметра фигуры"""
    fig = Circle(a)
    assert fig.perimeter() == perimeter


@pytest.mark.parametrize(("a", "new_fig", "new_area"),
                         [
                             (1, Rectangle(1, 2), math.pi + 2),
                             (3, Square(1), 9 * math.pi + 1),
                             (2, Triangle(5, 3, 4), 4 * math.pi + 6),
                             (10, Circle(7), 149 * math.pi),
                             (1, 44, 'Ошибка. В метод передана не фигура')
                         ])
def test_add_area(a, new_fig, new_area):
    """Проверка метода добавления площади новой фигуры к площади текущей"""
    fig = Circle(a)
    add_a = fig.add_area(new_fig)
    assert add_a == new_area
