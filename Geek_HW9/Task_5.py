# Реализуйте базовый класс Car.
#
# при создании класса должны быть переданы атрибуты: color (str), name (str).
# реализовать в классе методы: go(speed), stop(), turn(direction),
# которые должны изменять состояние машины - для хранения этих свойств вам понадобятся дополнительные атрибуты
# - придумайте какие.
# добавьте метод is_police() - который возвращает True/False,
# в зависимости от того является ли этот автомобиль полицейским (см.дальше)
# Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
# Добавьте в базовый класс метод get_status(), который должен возвращать
# в виде строки название, цвет, текущую скорость автомобиля и направление движения (в случае если автомобиль едет),
# для полицейских автомобилей перед названием автомобиля должно идти слово POLICE;
# Для классов TownCar и WorkCar в методе get_status()
# рядом со значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!",
# если скорость превышает 60 (TownCar) и 40 (WorkCar).
# Создайте по одному экземпляру каждого производного класса.
# В цикле из 10 итераций, для каждого автомобиля сделайте одно из случайных
# действий: go, stop, turn со случайными параметрами.
# После каждого действия показывайте статус автомобиля.


class Car:
    def __init__(self, color: str, name: str, is_police: bool = None):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, go: bool = None):
        self.go = go

    def stop(self, is_stop: bool = None):
        self.is_stop = is_stop

    def turn(self, direction: str = None):
        self.direction = direction

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость автомобиля: {self.speed}')

    def get_status(self):
        if self.go:
            print(f'Название автомобиля: {self.name}, цвет: {self.color}, скорость: {self.speed}, данная машина едет {self.direction}')
        else:
            print(f'Название автомобиля: {self.name}, цвет: {self.color}, скорость: {self.speed}, данная машина стоит, движется в направлении: {self.direction}')


class TownCar(Car):
    def __init__(self, color, name, speed):
        super().__init__(color, name)
        self.speed = speed

    def show_speed(self):
        if self.speed >= 60:
            print(f'Превышение!!! Скорость автомобиля равна: {self.speed}')
        else:
            print(f'Скорость автомибял равна: {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, color, name, speed):
        super().__init__(color, name)
        self.speed = speed

    def show_speed(self):
        if self.speed >= 40:
            print(f'Превышение!!! Скорость автомобиля равна: {self.speed}')
        else:
            print(f'Скорость автомобиля равна: {self.speed}')



class PoliceCar(Car):
    def get_status(self):
        if self.is_police == True:
            return print(f'Police {self.name} цвет {self.color} скорость автомобиля {self.speed} {self.direction}')
        else:
            return print(f'{self.name} цвет {self.color} скорость автомобиля {self.speed} {self.direction}')


car_1 = TownCar('red', 'Town', 50)
car_1.go(True)
car_1.show_speed()
# car_1.stop(False)
car_1.turn('Moscow')
car_1.get_status()

# car_1.get_status()

car_2 = PoliceCar('black', 'Kuku')
car_2.go(False)
car_2.turn('SPB')
# car_2.get_status()
