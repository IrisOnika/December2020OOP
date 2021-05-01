import math
from fig_class import Fig


class Rectangle(Fig):
    """класс прямоугольник. для создания нужно задать длину двух перпендикулярных сторон"""

    name = 'rectangle'
    angles = 4

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def area(self):
        s = self.a * self.b
        return print(f'Площадь прямоугольника равна {s}')

    def perimeter(self):
        p = 2*(self.a + self.b)
        return print(f'Периметр прямоугольника равен {p}')

    def info(self):
        if self.a > 0:
            if self.b > 0:
                return print(f'прямоугольник со сторонами {self.a}, {self.b}')
            else:
                print('в прямоугольнике сторона b задана некорректно. введите положительное число')
        else:
            print('в прямоугольнике сторона a задана некорректно. введите положительное число')


class Square(Fig):
    """ класс квадрат. для создания нужно задать длину одной из сторон"""

    name = 'square'
    angles = 4

    def __init__(self, a):
        self.a = a

    def get_a(self):
        return self.a

    def area(self):
        s = self.a ** 2
        return print(f'Площадь квадрата равна {s}')

    def perimeter(self):
        p = 4 * self.a
        return print(f'Периметр квадрата равен {p}')

    def info(self):
        if self.a > 0:
            return print(f'квадрат со сторонами {self.a}')
        else:
            return print('в квадрате сторона a задана некорректно. введите положительное число')


class Triangle(Fig):
    """класс треугольник. для создания нужно задать длину каждой из трёх сторон"""
    name = 'triangle'
    angles = 3

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def area(self):
        half_p = (self.a + self.b + self.c) / 2.0
        s = (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5
        return print(f'Площадь квадрата равна {s}')

    def perimeter(self):
        p = self.a + self.b + self.c
        return print(f'Периметр квадрата равен {p}')

    def info(self):
        if self.a > 0:
            if self.b > 0:
                if self.c > 0:
                    if (self.a + self.b > self.c) & (self.a + self.c > self.b) & (self.b + self.c > self.a):
                        return print(f'треугольник со сторонами {self.a}, {self.b}, {self.c}')
                    else:
                        return print('в треугольнике сумма двух любых сторон должна быть больше третьей стороны')
                else:
                    return print('в треугольнике сторона c задана некорректно. введите положительное число')
            else:
                return print('в треугольнике сторона b задана некорректно. введите положительное число')
        else:
            return print('в треугольнике сторона a задана некорректно. введите положительное число')


class Circle(Fig):
    """ класс круг. для создания нужно задать радиус"""

    name = 'circle'
    angles = 0

    def __init__(self, a: float):
        self.a = a

    def get_a(self):
        return self.a

    def area(self):
        s = math.pi * (self.a ** 2)
        return print(f'Площадь круга равна {s}')

    def perimeter(self):
        p = 2 * math.pi * self.a
        return print(f'Периметр круга равен {p}')

    def info(self):
        if self.a > 0:
            return print(f'круг с радиусом {self.a}')
        else:
            return print('радиус круга задан некорректно. введите положительное число')
