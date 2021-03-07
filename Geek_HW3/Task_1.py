# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

def num_translate(elem):
    if elem in numerals:
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

num_translate('one')
