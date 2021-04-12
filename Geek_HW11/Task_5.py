# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь)


class Storage:
    def __init__(self):
        self.storage = {}

    def add(self, office_equipment, department: str):
        self.storage.setdefault(department, [])
        self.storage[department].append(office_equipment)

    def remove_eqiupment(self, office_equipment, department):
        self.storage[department].remove(office_equipment)

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


class Printer(Office_equipment):
    def __init__(self, price, weight, name, print_speed: int):
        super().__init__(price, weight, name)
        self.print_speed = print_speed


class Scanner(Office_equipment):
    def __init__(self, price, weight, name, scan_speed: int):
        super().__init__(price, weight, name)
        self.speed_of_scan = scan_speed


class Copier(Office_equipment):
    def __init__(self, price, weight, name, copy_speed: int):
        super().__init__(price, weight, name)
        self.copy_speed = copy_speed


if __name__ == '__main__':
    storage = Storage()
    scanner = Scanner(20000, 10, 'SUMSUNG', 30)
    storage.add(scanner, 'Отдел продаж')
    print(storage.storage)
    storage.move(scanner, 'Отдел продаж', 'Офис')
    print(storage.storage)
