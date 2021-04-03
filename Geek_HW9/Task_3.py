# Реализовать базовый класс Employee (сотрудник).
#
# определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
# создать класс Position (должность) с аттрибутами employee (сотрудник/Employee),
# position (должность/str), income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# в классе Position реализовать методы получения полного имени сотрудника get_full_name()
# и дохода с учётом премии get_total_income() (wage + bonus);
# проверить работу примера на реальных данных: создать экземпляры классов Employee, Position,
# вывести на экран имя сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position.


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position(Employee):
    _income = {
        'wage': None,
        'bonus': None
    }

    def __init__(self, name: str, surname: str, position: str = None, income_wage=None, income_bonus=None):
        super().__init__(name, surname)
        self.position = position
        self._income['wage'] = income_wage
        self._income['bonus'] = income_bonus

    def get_full_name(self):
        return print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        result = 0
        if self._income['bonus'] is None:
            result = self._income['wage']
        else:
            for val in self._income.values():
                result += val
        print(f'Доход сотрудника {self.name} {self.surname} на должности {self.position} составляет : {result} $')
        return result


worker = Position('Ivan', 'Ivanovich', 'Manager', 12, 45)
worker.get_full_name()
worker.get_total_income()


# PS не сильно понял формулировку с income
