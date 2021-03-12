import requests
from requests import utils
from decimal import *
from datetime import datetime


def get_currency_rate(currency_code):

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    if 'Date="' in content:
        cut = content.index('Date="')
        temp_date = content[cut + 6:cut + 16].split('.')
        bank_date = datetime(year=int(temp_date[2]), month=int(temp_date[1]), day=int(temp_date[0]))

    if currency_code in content:
        cut = content.index(currency_code)
        content = content[cut:]

        if '<Value>' in content:
            cut = content.index('<Value>')
        content = content[cut + 7:cut + 17].split('<')
        currency = Decimal(float(content[0].replace(',', '.')))
        print(f"{currency_code} {currency:6.4} {bank_date.strftime('%Y-%m-%d')}")

    else:
        print('None')
        exit(0)


user_value = str.upper(input('Введите, какой курс вас интересует? '))
get_currency_rate(user_value)