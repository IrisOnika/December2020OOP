from abc import ABC, abstractmethod
from figs import Rectangle, Square, Circle, Triangle


class Fig(ABC):
    """ класс геометрическая фигура """

    name: str
    angles: int

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def angles(self):
        pass

    def add_area(self, name, a, b=None, c=None):

        if name == 'rectangle':
            new_fig = Rectangle(a, b)
            if new_fig.info() == f'прямоугольник со сторонами {new_fig.get_a()}, {new_fig.get_b()}':
                return print(f'площадь двух фигур равна {self.area() + new_fig.area()}')
            else:
                return new_fig.info()
        elif name == 'square':
            new_fig = Square(a)
            if new_fig.info() == f'квадрат со сторонами {new_fig.get_a()}':
                return print(f'площадь двух фигур равна {self.area() + new_fig.area()}')
            else:
                return new_fig.info()
        elif name == 'circle':
            new_fig = Circle(a)
            if new_fig.info() == f'круг с радиусом {new_fig.get_a}':
                return print(f'площадь двух фигур равна {self.area() + new_fig.area()}')
            else:
                return new_fig.info()
        elif name == 'triangle':
            new_fig = Triangle(a, b, c)
            if new_fig.info() == f'треугольник со сторонами {new_fig.get_a}, {new_fig.get_b}, {new_fig.get_c}':
                return print(f'площадь двух фигур равна {self.area() + new_fig.area()}')
            else:
                return new_fig.info()
        else:
            return print("задайте одну из следующих фигур: "
                         "прямоугольник - 'rectangle', квадрат - 'square', круг - 'circle', треугольник - 'triangle'")









        pass
