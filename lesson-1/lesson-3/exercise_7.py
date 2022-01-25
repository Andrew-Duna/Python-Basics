__author__ = 'Болотов Андрей Вячеславович'
"""
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Используйте написанную ранее функцию int_func().
"""
import exercise_6


def divide(args):
    my_list = args.split()
    for i in range(len(my_list)):
        my_list[i] = exercise_6.int_func(my_list[i])
    return ' '.join(my_list)


if __name__ == '__main__':
    my_str = input('Введите строку - ')
    print(divide(my_str))
