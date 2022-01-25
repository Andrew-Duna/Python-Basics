__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(dividend, divider):
    try:
        result = dividend / divider
    except ZeroDivisionError as error:
        print(error, '\nНа 0 делить нельзя')
        result = None
    return result


if __name__ == '__main__':
    num_1 = input('Введите делимое знначение : ')
    while not num_1.isdigit():
        num_1 = input('Это должно быть число!\n')
    num_2 = input('Введите делитель : ')
    while not num_2.isdigit():
        num_2 = input('Это должно быть число!\n')

    print(f'{division(int(num_1), int(num_2)):.2f}')
