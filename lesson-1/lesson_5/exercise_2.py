__author__ = 'Болотов Андрей Вячеславович'
"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

with open('for_second_exercise.txt', encoding='UTF-8') as f:
    ls = f.readlines()
    print(f'Количество строк в файле - {len(ls)}')
    for i, line in enumerate(ls, 1):
        print(f'{i} строка содержит {len(line)} элиментов')
