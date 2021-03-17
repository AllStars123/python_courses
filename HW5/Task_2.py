# Создайте объект-генератор, выбирающий из функции-генератора rand_nums,
# написанного в предыдущем задании, только нечетные числа.
# Проитерируйтесь по этому объекту-генератору и выведите на экран для каждого значения на отдельной строке:
# порядковый номер (начиная с 1-го) и соответствующее ему значение.
# Например:
# 1 11
# ...
# 10 7

from random import randint


def rand_nums(max_rand):
    for _ in range(max_rand):
        yield randint(0, 100)


rand_count = 41
rand15 = rand_nums(rand_count)

for _ in range(1, rand_count + 1):
    next_number = next(rand15)
    gen_odd_numbers = (print(_, next_number, sep=" ") if next_number % 2 == 1 else print('Число чётное'))


# В rand_nums надо передать всегда разное(так как это рандом)