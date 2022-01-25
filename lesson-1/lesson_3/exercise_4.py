__author__ = 'Болотов Андрей Вячеславович'
"""
Программа принимает действительное положительное число x и целое отрицательное число y. 
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def test_base(args):
    while True:
        try:
            args = float(args)
            if args >= 0:
                return args
            else:
                args = input('Число должно быть положителным - ')
                continue
        except ValueError:
            args = input('Повторите ввод число. Число должно быть действительное и положительное (Пример 25.5, 4) - ')
            continue


def test_exponent(args):
    while True:
        try:
            args = int(args)
            if args < 0:
                return args
            else:
                args = input('Число должно быть отрицатеньным - ')
                continue
        except ValueError:
            args = input('Повторите ввод число.Число должно быть целое и отрицательное(Пример -4, -55) - ')
            continue


def exponentiation_1(x, y):
    return x ** y


def exponentiation_2(x, y):
    if y == 0:
        return 1
    else:
        return 1 / x * exponentiation_2(x, y + 1)


def exponentiation_3(x, y):
    i = 1
    while y < 0:
        i *= x
        y += 1
    return 1 / i


if __name__ == '__main__':
    a = input('Введите число которое ввести в сепень. x = ')
    a = test_base(a)
    b = input('Введите степень в которую необходимо возвести число "х" (она должна быть отрицательным). y = ')
    b = test_exponent(b)
    print(f'{exponentiation_1(a, b):.03f}')
    print(f'{exponentiation_2(a, b):.03f}')
    print(f'{exponentiation_3(a, b):.03f}')
