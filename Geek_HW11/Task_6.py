# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Mistake(Exception):
    pass


class Storage:
    def __init__(self):
        self.storage = {}

    def add(self, office_equipment, department: str):
        self.storage.setdefault(department, [])
        self.storage[department].append(office_equipment)

    def remove_eqiupment(self, office_equipment, department):
        try:
            self.storage[department].remove(office_equipment)
        except:
            raise Mistake(f'{office_equipment} нет на складе')

    def move(self, office_equipment, department_from, department_to):
        self.remove_eqiupment(office_equipment, department_from)
        self.add(office_equipment, department_to)


class Office_equipment():
    def __init__(self, price: int, weight: int, name: str):
        self.price = price
        self.weight = weight
        self.name = name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return self.price + other.price

    def checker(self):
        if type(self.price) != int:
            raise Mistake('Цену товара нужно вводить цифрами')
        if type(self.weight) != int:
            raise Mistake('Вес товара нужно вводить цифрами')
        if type(self.name) != str:
            raise Mistake('Название товара нужно вводить цифрами')


class Printer(Office_equipment):
    def __init__(self, price, weight, name, print_speed: int):
        super().__init__(price, weight, name)
        super().checker()
        self.print_speed = print_speed


class Scanner(Office_equipment):
    def __init__(self, price, weight, name, scan_speed: int):
        super().__init__(price, weight, name)
        super().checker()
        self.speed_of_scan = scan_speed


class Copier(Office_equipment):
    def __init__(self, price, weight, name, copy_speed: int):
        super().__init__(price, weight, name)
        super().checker()
        self.copy_speed = copy_speed


if __name__ == '__main__':
    storage = Storage()
    scanner = Scanner(20000, 10, 'SUMSUNG', 30)
    printer = Printer(5000, 20, 'HP', 40)
    storage.add(scanner, 'Отдел продаж')
    print(storage.storage)
    storage.move(scanner, 'Отдел продаж', 'Офис')
    print(storage.storage)
    print('Цена двух товаров составляет:', scanner + printer)
