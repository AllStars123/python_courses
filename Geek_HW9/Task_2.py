# Реализовать класс Road (дорога).
#
# определить защищенные атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# определить внутри класса приватную константу масса квадратного метра асфальта толщиной 1 см.
# определить метод расчёта массы асфальта get_asphalt_mass(height),
# необходимого для покрытия всей дороги толщиной height см;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв.
# метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_mass(self, height):
        __asphalt_mass = 25
        result = (self._length * self._width * height * __asphalt_mass) / 1000
        print(f'{self._length} м * {self._width} м * {__asphalt_mass} кг * {height} см = {round(result)} т')
        return result


road_1 = Road(450, 5000)
road_1.get_asphalt_mass(5)

road_2 = Road(56, 3758)
road_2.get_asphalt_mass(4)



