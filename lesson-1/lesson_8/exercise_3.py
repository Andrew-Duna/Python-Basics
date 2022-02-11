__author__ = 'Болотов Андрей Вячеславович'
"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на отсутствие элементов
типа строка и булево. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnException(Exception):
    def __init__(self):
        self.txt = "Некорректный тип данных! Необходимо ввести число!"


if __name__ == '__main__':
    mylist = []
    input_string = input('Введите число. Для выхода введите пустую строку: ')
    while input_string:
        try:
            if input_string.isdigit():
                mylist.append(int(input_string))
            else:
                raise OwnException
        except OwnException as e:
            print(e.txt)
        input_string = input('Введите число. Для выхода введите пустую строку: ')
    print(mylist)
