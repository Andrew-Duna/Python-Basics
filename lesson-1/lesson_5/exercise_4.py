__author__ = 'Болотов Андрей Вячеславович'
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

my_dist = {'one': 'Одиин', 'two': 'Два', 'three': 'Три', 'four': 'Четыре'}
with open('for_fourth_exercise.txt', encoding='UTF-8') as f_1:
    with open('for_fourth_exercise_new.txt', 'w', encoding='UTF-8') as f_2:
        for i in f_1.readlines():
            el_1, el_2 = i.split(' — ')
            f_2.write(f'{my_dist[el_1.lower()]} - {el_2}')
