from abc import ABC, abstractmethod


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

    def add_area(self, new_fig):
        if str(type(new_fig)) == "<class 'figure.figs.Rectangle'>" \
                or str(type(new_fig)) == "<class 'figure.figs.Square'>" \
                or str(type(new_fig)) == "<class 'figure.figs.Triangle'>" \
                or str(type(new_fig)) == "<class 'figure.figs.Circle'>":
            if self.area() != 'параметры фигуры заданы некорректно':
                if new_fig.area != 'параметры фигуры заданы некорректно':
                    print(self.area())
                    print(new_fig.area())
                    new_area = self.area() + new_fig.area()
                    return new_area
                else:
                    print(new_fig.area())
                    return 'параметры новой фигуры заданы некорретно'
            else:
                return 'параметры исходной фигуры заданы некорретно'
        else:
            return 'Ошибка. В метод передана не фигура'
