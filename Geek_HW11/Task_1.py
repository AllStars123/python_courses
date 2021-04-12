# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data: str):
        self.day, self.month, self.year = self.parse_int(data)
        self.valid(self.day, self.month, self.year)

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    @classmethod
    def parse_int(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            pass
        else:
            raise ValueError('Вы ввели некорректный день')
        if 1 <= month <= 12:
            pass
        else:
            raise ValueError('Вы ввели некорректый месяц')
        if year > 0:
            pass
        else:
            raise ValueError('Выввели отрицательный год')


if __name__ == '__main__':
    mc = Data('12-3-2045')
    print(mc)
