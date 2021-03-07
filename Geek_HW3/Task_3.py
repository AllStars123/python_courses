# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
#
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?


def thesaurus(*args):
    names = {}
    for elem in args:
        word_1 = elem[0]
        names.setdefault(word_1, [])
        names[word_1].append(elem)
    return names


sort_dict = thesaurus("Иван", "Мария", "Петр", "Илья", "Арсений")

for first_letter in sorted(sort_dict.keys()):
    print(f'{first_letter} : {sort_dict[first_letter]}')
