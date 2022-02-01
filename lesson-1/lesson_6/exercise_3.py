__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотлудника {self.surname} {self.name} ')

    def get_total_income(self):
        print(f'Полная ЗП сотрудника - {self.income["wage"] + self.income["bonus"]}')


if __name__ == '__main__':
    man = Position('Иван', 'Пупкин', 'mover', 20000, 5000)
    man.get_full_name()
    man.get_total_income()
