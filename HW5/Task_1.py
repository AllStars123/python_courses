# Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно).
# Количество чисел N, которое выдаст генератор передается в функцию через параметр:
#
# >>> rand15 = rand_nums(15)
# >>> next(rand15) # 1-й вызов
# 11
# >>> next(rand15) # 2-й вызов
# 38
# ...
# >>> next(rand15) # 15-й вызов
# 7
# >>> next(rand15) # 16-й вызов
# ...StopIteration...

from random import randint


def rand_nums(max_rand):
    for i in range(max_rand):
        random_number = randint(0, 100)
        yield random_number


rand15 = rand_nums(15)
print(next(rand15))

# print(*islice(rand15, 10))
