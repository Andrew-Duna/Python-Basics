__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, 
проверить на практике работу декоратора @property.
"""


class Сlothes:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани - {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Сlothes):
    @property
    def get_square(self):
        return round(self.width / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Площадь на пальто {self.get_square}'


class Costume(Сlothes):
    @property
    def get_square(self):
        return round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Площадь на костюм {self.get_square}'


if __name__ == '__main__':
    coat = Coat(2, 4)
    сostume = Costume(1, 2)
    print(coat)
    print(сostume)
    print(coat.get_sq_full)
    print(сostume.get_sq_full)
    print(coat.get_square)
    print(сostume.get_square)
