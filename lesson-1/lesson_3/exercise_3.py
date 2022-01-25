__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""


def my_func(args_1, args_2, args_3):
    if args_1 >= args_2:
        return args_1 + args_2 if args_2 >= args_3 else args_1 + args_3
    else:
        return args_1 + args_2 if args_1 >= args_3 else args_2 + args_3


if __name__ == '__main__':
    print(my_func(1, 2, 3))  # return 5
