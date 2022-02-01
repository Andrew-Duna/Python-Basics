__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('«Запуск отрисовки»')


class Pen(Stationery):
    def draw(self):
        print('«Запуск отрисовки» - Ручкой')


class Pencil(Stationery):
    def draw(self):
        print('«Запуск отрисовки - Карандашем»')


class Handle(Stationery):
    def draw(self):
        print('«Запуск отрисовки - маркером»')


if __name__ == '__main__':
    stationery = Stationery('Петя')
    pen = Pen('Вася')
    pencil = Pencil('Маша')
    handle = Handle('Валера')
    print(stationery.title)
    stationery.draw()
    print(pen.title)
    pen.draw()
    print(pencil.title)
    pencil.draw()
    print(handle.title)
    handle.draw()
