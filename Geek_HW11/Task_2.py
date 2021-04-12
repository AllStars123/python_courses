# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_division_by_zero(Exception):
    pass


def div(a, b):
    if b == 0:
        raise My_division_by_zero('Делить на 0 нельзя')
    return print(a / b)


if __name__ == '__main__':
    try:
        div(2, 0)
    except My_division_by_zero as M:
        print(M)
