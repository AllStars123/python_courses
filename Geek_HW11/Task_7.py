# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# class Complex:
#     def __init__(self, number: complex):
#         self.number = number
#
#     def __add__(self, other):
#         return self.number + other.number
#
#     def __mul__(self, other):
#         return self.number * other.number
#
#
# if __name__ == '__main__':
#     num1 = Complex(complex(1, 2))
#     num2 = Complex(complex(1, 2))
#     print(num1.number)
#     print(num1 + num2)
#     print(num1 * num2)

# PS. Это решение совсем простое, поэтому сделал 2 варианта


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real}{self.imaginary:+}i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)


if __name__ == '__main__':
    num1 = Complex(1, 2)
    num2 = Complex(1, 2)
    print(num1 + num2)
    print(num1 * num2)

    test1 = complex(1, 2)
    test2 = complex(1, 2)
    z = test1 + test2
    z1 = test1 * test2
    print(z)
    print(z1)
