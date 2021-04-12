# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Storage:
    def __init__(self):
        self.storage = {}


class Office_equipment():
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight


class Printer(Office_equipment):
    def __init__(self, price, weight, print_speed):
        super().__init__(price, weight)
        self.print_speed = print_speed


class Scanner(Office_equipment):
    def __init__(self, price, weight, scan_speed):
        super().__init__(price, weight)
        self.speed_of_scan = scan_speed


class Copier(Office_equipment):
    def __init__(self, price, weight, copy_speed):
        super().__init__(price, weight)
        self.copy_speed = copy_speed
