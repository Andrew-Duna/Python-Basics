__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать класс Matrix (матрица). 
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для 
формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем 
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        result = []
        if self.matrix == other.matrix:
            for i in range(len(self.matrix)):
                result.append([])
                if self.matrix[i] == other.matrix[i]:
                    for j in range(len(self.matrix[i])):
                        result[i].append(self.matrix[i][j] + other.matrix[i][j])
                else:
                    return f'Матрицы разной размерности'
            return Matrix(result)
        else:
            return f'Матрицы разной размерности'


if __name__ == '__main__':
    vector_1 = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
    vector_2 = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
    matrix_1 = Matrix(vector_1)
    matrix_2 = Matrix(vector_2)
    print(matrix_1 + matrix_2)
