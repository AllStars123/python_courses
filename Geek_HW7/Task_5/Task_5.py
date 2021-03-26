#  Написать скрипт, который выводит статистику для заданной папки в виде словаря,
#  в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]),
#  например:
#
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
import os
import json


root_dir = '/Users/nikitapurnov/PycharmProjects/Geek HW/Geek_HW2'

tuple_value = ()
types = []
size_count = {}
for root, dirs, files in os.walk(root_dir):
    stat = os.stat(root).st_size
    lk = len([name for name in os.listdir(root) if os.path.isfile(os.path.join(root, name))])
    types = []

    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        if ext not in types:
            types.append(ext)

        gn = list(tuple_value)
        gn.append(lk)
        gn.append(types)
        size_count[stat] = gn

for key, val in size_count.items():
    print(f'{key} : {val}')


name_json = root_dir.split('/')

with open(f'{name_json[5]}_summary.json', 'w') as f:
    json.dump(size_count, f)