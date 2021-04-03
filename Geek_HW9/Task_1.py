# Создать класс TrafficLight (светофор).
#
# определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
# после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью:
# красный (3 сек), жёлтый (1 сек), зелёный (3 сек);
# переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
# проверить переключение режимов работы светофора,
# опрашивая в цикле текущее состояние светофора с интервалом 0.5 секунды,
# используя метод get_current_signal()


import random
from time import sleep
from time import time
from multiprocessing import Process


class TrafficLight:

    def __init__(self, color):
        self.color = color

    def light(self, colors):
        for i in colors:
            if i == 'red':
                sleep(3)
                self.color = i
            elif i == 'yellow':
                sleep(1)
                self.color = i
            else:
                sleep(3)
                self.color = i

    def traffic(self):
        t_end = time() + 20
        while time() < t_end:
            if self.color == 'red':
                colors = ['red', 'yellow', 'green']
                self.light(colors)

            elif self.color == 'yellow':
                colors = ['yellow', 'green', 'red']
                self.light(colors)

            else:
                colors = ['green', 'red', 'yellow']
                self.light(colors)

    def show_color(self):
        t_end = time() + 20
        while time() < t_end:
            amount = random.randint(1, 2)
            sleep(amount)
            print(self.color)


if __name__ == '__main__':
    p1 = TrafficLight('red')

    thread1 = Process(target=p1.traffic)
    thread1.start()
    thread2 = Process(target=p1.show_color())
    thread2.start()
