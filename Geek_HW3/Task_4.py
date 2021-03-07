#  (вместо задачи 3) Написать функцию thesaurus_adv(),
#  принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
#  в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и
#  содержащие записи, в которых фамилия начинается с соответствующей буквы.
#  Например:
#
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }


def thesaurus(*args):
    people = {}
    for elem in args:
        name, last_name = elem.split()
        first_letter_name = name[0]
        first_letter_last_name = last_name[0]
        people.setdefault(first_letter_last_name, {}).setdefault(first_letter_name, []).append(elem)

    return people


sort_dict = thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

for first_letter_last_name in sorted(sort_dict.keys()):
    print(f'"{first_letter_last_name}":')
    for first_letter_name in sorted(sort_dict[first_letter_last_name].keys()):
        print(f'    "{first_letter_name}":{sort_dict[first_letter_last_name][first_letter_name]}')

