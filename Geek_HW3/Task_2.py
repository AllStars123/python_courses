# (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы.
# Например:
#
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(elem):
    if elem in numerals:
        if res.istitle():
            print(numerals[elem].title())
        else:
            print(numerals[elem])
    else:
        print(None)


numerals = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}

res = 'One'
res_low = res.lower()

# res = input()
# res_low = res.lower()

num_translate_adv(res_low)