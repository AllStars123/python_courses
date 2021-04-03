# Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw() (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры каждого класса и положить их в список.
# Проитерироваться по этому списку и вызвать метод draw() для каждого элемента.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера')


list_of_object = []

obj_1 = Stationery('Penal')
obj_2 = Pen('Ручка')
obj_3 = Pencil('Карандаш')
obj_4 = Handle('Маркер')

list_of_object.append(obj_1)
list_of_object.append(obj_2)
list_of_object.append(obj_3)
list_of_object.append(obj_4)

for i in list_of_object:
    i.draw()
