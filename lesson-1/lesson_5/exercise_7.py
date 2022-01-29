__author__ = 'Болотов Андрей Вячеславович'
"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: 
    название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

my_dict = {}
all_profit = []
with open('for_seventh_exercise.txt', encoding='utf-8') as f:
    for ls in f.readlines():
        info_firm = ls.split()
        profit = int(info_firm[2]) - int(info_firm[3])
        if profit > 0:
            all_profit.append(profit)
            my_dict.update({info_firm[0]: profit})
        else:
            my_dict.update({info_firm[0] + ' Убытки': profit})
    result = [my_dict, {'average_profit': sum(all_profit) / len(all_profit)}]
with open('my_file.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
