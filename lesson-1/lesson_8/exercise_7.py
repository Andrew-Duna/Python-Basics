__author__ = 'Болотов Андрей Вячеславович'
"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"

if __name__ == '__main__':
    my_complex_number_1 = Complex(9, 5)
    my_complex_number_2 = Complex(-5, 6)
    print(f"Сумма: {my_complex_number_1 + my_complex_number_2}")
    print(f"Произведение: {my_complex_number_1 * my_complex_number_2}")

    my_number_1 = complex(9, 5)
    my_number_2 = complex(-5, 6)
    print(my_number_1 + my_number_2)
    print(my_number_1 * my_number_2)
