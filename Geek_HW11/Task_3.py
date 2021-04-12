# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка

class Check(Exception):
    pass


def word_is_digit():
    digit = []
    while True:
        a = input('Введите число:')

        if a.isdigit():
            convert = int(a)
            digit.append(convert)
            print(digit)

        elif a == 'stop':
            print(digit)
            break

        else:
            raise Check('Вы ввели что-то непонятное')
    return digit


if __name__ == '__main__':

    try:
        word_is_digit()
    except Check as c:
        print(c)
