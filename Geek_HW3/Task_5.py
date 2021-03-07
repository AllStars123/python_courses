# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов,
# взятых из трёх списков (по одному слову из каждого списка):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
#
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?


from random import choice
def get_jokes(tmp, unikum = False):

    """
    Функция возращает шутки в виде списка строк
    :param unikum : bool удаляет повторы из шуток
    :param main_list : list список где хранятся шутки
    :param list_with_jokes : хранит список шуток ввиде строки
    :return возвращает список с шутками
    """

    list_with_jokes = []
    for i in range(tmp):
        main_list = []

        first_word = choice(nouns)
        main_list.append(first_word)

        second_word = choice(adverbs)
        main_list.append(second_word)

        third_word = choice(adjectives)
        main_list.append(third_word)

        joke = ' '.join(main_list)
        list_with_jokes.append(joke)

        if unikum:
            nouns.remove(first_word)
            adverbs.remove(second_word)
            adjectives.remove(third_word)

    return list_with_jokes



nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(5, True))

