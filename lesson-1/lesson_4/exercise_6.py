__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее. 
Подсказка: используйте функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Предусмотрите условие его завершения. 
#### Например, в первом задании выводим целые числа, начиная с 3. 
При достижении числа 10 — завершаем цикл. 
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count, cycle


def generator(num):
    for i in count(num):
        if i > num + 10:
            break
        else:
            yield i


def repeating_element(list):
    cound = 1
    for i in cycle(list):
        if cound > (len(list) * 2):
            break
        else:
            yield i
            cound += 1


if __name__ == '__main__':
    num = 10  # Указываем с какого числа начать
    my_list = [i for i in generator(num)]
    print('Полученный список - ', *my_list)
    repeat_list = [i for i in repeating_element(my_list)]
    print('Список повторяющийся 2 раза  - ', *repeat_list)
