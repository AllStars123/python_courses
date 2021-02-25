# Сумма чисел из списка *
#
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):
# 1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# 2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
# сумма цифр которых делится нацело на 7.
# 3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков

# без списка
summa = 0
for i in range(1000):
    if i % 2 == 1:
        odd_numbers = i ** 3
        summa_of_number = 0
        copy = odd_numbers
        while odd_numbers != 0:
            digit = odd_numbers % 10
            summa_of_number = summa_of_number + digit
            odd_numbers = odd_numbers // 10
        if summa_of_number % 7 == 0:
            summa = summa + copy
    i += 1
print('Сумма всех элементов равна: ', summa)

# без списка, +17
summa = 0
for i in range(1000):
    if i % 2 == 1:
        odd_numbers = i ** 3 + 17
        summa_of_number = 0
        copy = odd_numbers
        while odd_numbers != 0:
            digit = odd_numbers % 10
            summa_of_number = summa_of_number + digit
            odd_numbers = odd_numbers // 10
        if summa_of_number % 7 == 0:
            summa = summa + copy
    i += 1
print('Сумма всех элементов после прибавления 17 к каждому элементу равна: ', summa)

# Со списком
some_List = []
new_List = []
for i in range(1000):
    if i % 2 == 1:
        some_List.append(i ** 3)
for number in some_List:
    sum_of_number = 0
    copy = number
    while number != 0:
        digit = number % 10
        sum_of_number = sum_of_number + digit
        number = number // 10
    if sum_of_number % 7 == 0:
        new_List.append(copy)
print('Сумма: ', sum(new_List))
# print(some_List)
# print(newList)

