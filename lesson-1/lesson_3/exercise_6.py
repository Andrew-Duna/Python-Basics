__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
"""


def int_func(args):
    return args.capitalize()


if __name__ == '__main__':
    my_str = input('Введите одно слово - ')
    print(int_func(my_str))
