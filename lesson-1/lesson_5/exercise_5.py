__author__ = 'Болотов Андрей Вячеславович'
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
from random import randint

num_rep = 10  # Количество вводимых чисел
with open('for_fifth_exercise.txt', 'w+', encoding='utf-8') as f:
    for i in range(num_rep):
        f.write(str(randint(0, 10)) + ' ')
    f.seek(0)
    print(f'Список - {f.read()}')
    f.seek(0)
    sum_ls = sum(int(i) for i in f.read().split())
    print(f'Сумма чисел  - {sum_ls}')
