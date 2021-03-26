# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
# например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
#
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os


folder = '/Users/nikitapurnov/PycharmProjects/Geek HW/Test_lessons'
size_count = {}
for root, dirs, files in os.walk(folder):
    stat = os.stat(root).st_size
    size_count[stat] = len([name for name in os.listdir(root) if os.path.isfile(os.path.join(root, name))])

for key, val in size_count.items():
    print(f'{key} : {val}')
