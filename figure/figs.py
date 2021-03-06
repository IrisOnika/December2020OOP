import math
from figure.fig_class import Fig


class NotPositiveSideError(Exception):
    """Вызвывается, когда задано не положительное число"""
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectTriangleSideError(Exception):
    """Вызывается, когда две стороны треугольника меньше третьей"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Rectangle(Fig):
    """класс прямоугольник. для создания нужно задать длину двух перпендикулярных сторон"""

    name = 'rectangle'
    angles = 4

    def __init__(self, a: float, b: float):
        try:
            if a > 0 and b > 0:
                self.a = a
                self.b = b
            else:
                raise NotPositiveSideError('одна из сторон не является положительным числом')
        except AttributeError as er:
            print(er)
        except TypeError as er:
            print(er)

    def area(self):
        if self.a > 0 and self.b > 0:
            s = self.a * self.b
            return s
        else:
            return 'параметры фигуры заданы некорректно'

    def perimeter(self):
        if self.a > 0 and self.b > 0:
            p = 2*(self.a + self.b)
            return p
        else:
            return 'параметры фигуры заданы некорректно'

    def info(self):
        return print(f'прямоугольник со сторонами {self.a}, {self.b}')


class Square(Fig):
    """ класс квадрат. для создания нужно задать длину одной из сторон"""

    name = 'square'
    angles = 4

    def __init__(self, a: float):
        try:
            if a > 0:
                self.a = a
            else:
                raise NotPositiveSideError('сторона не является положительным числом')
        except AttributeError as er:
            print(er)
        except TypeError as er:
            print(er)

    def area(self):
        s = self.a ** 2
        return s

    def perimeter(self):
        p = 4 * self.a
        return p

    def info(self):
        return print(f'квадрат со сторонами {self.a}')


class Triangle(Fig):
    """класс треугольник. для создания нужно задать длину каждой из трёх сторон"""
    name = 'triangle'
    angles = 3

    def __init__(self, a: float, b: float, c: float):
        try:
            if a > 0 and b > 0 and c > 0:
                if (a + b > c) and (a + c > b) and (b + c > a):
                    self.a = a
                    self.b = b
                    self.c = c
                else:
                    raise IncorrectTriangleSideError('сумма двух сторон треугольника меньше третьей')
            else:
                raise NotPositiveSideError('одна из сторон треугольнака не является положительным числом')
        except AttributeError as er:
            print(er)
        except TypeError as er:
            print(er)

    def area(self):
        half_p = (self.a + self.b + self.c) / 2.0
        s = (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5
        return s

    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    def info(self):
        return print(f'треугольник со сторонами {self.a}, {self.b}, {self.c}')


class Circle(Fig):
    """ класс круг. для создания нужно задать радиус"""

    name = 'circle'
    angles = 0

    def __init__(self, a: float):
        try:
            if a > 0:
                self.a = a
            else:
                raise NotPositiveSideError('радиус не является положительным числом')
        except AttributeError as er:
            print(er)
        except TypeError as er:
            print(er)

    def area(self):
        s = math.pi * (self.a ** 2)
        return s

    def perimeter(self):
        p = 2 * math.pi * self.a
        return p

    def info(self):
        return print(f'круг с радиусом {self.a}')
