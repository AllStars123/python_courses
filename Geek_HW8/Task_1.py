# Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?
import re


def email_parse(mail):
    split_email = {}
    re_email = re.compile(r'@[\w\.]+(\.[\w]+)+')
    check = re.search(re_email, mail)

    if not check:
        raise ValueError('wrong email')

    username, domain = re.split(r'@', mail)
    split_email[username] = domain

    for user, dom in split_email.items():
        print(f"'username': '{user}', 'domain': '{dom}'")


email_parse('someone@geekbrains.ru')
