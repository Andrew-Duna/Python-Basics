__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция вызывается следующим образом: for el in fact(n). 
Она отвечает за получение факториала числа. 
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from itertools import count, cycle


def fact(num):
    result = 1
    for i in count(1):
        if i > num:
            break
        else:
            result *= i
            yield result


if __name__ == '__main__':
    num = 5  # Число какого факториала найти
    my_list = [i for i in fact(num)]
    print('Факториал ', num, ' - ', *my_list)
