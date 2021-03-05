# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

main_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0

while index < len(main_list):
    obj = main_list[index]
    if obj.isdigit():
        main_list[index] = f'{int(obj):02d}'
        main_list.insert(index, '"')
        main_list.insert(index + 2, '"')
        index += 3
    elif (obj[0] == '+' or obj[0] == '-') and obj[1:].isdigit():
        plus_minus = obj[0]
        main_list[index] = f'{int(obj[1:]):02d}'
        main_list.insert(index, '"')
        main_list.insert(index + 2, '"')
        index += 3
    else:
        index += 1
result = ' '.join(main_list)
print(result)
