# Человеко-ориентированное представление интервала времени
#
# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
# 1) до минуты: <sec> сек;
# 2) до часа: <min> мин <sec> сек;
# 3) до суток: <count> час <min> мин <sec> сек;
# 4) сутки или больше: <day> дн <count> час <min> мин <sec> сек
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек

sec_in_min = 60
sec_in_hour = sec_in_min * 60  # 3600 sec
sec_in_day = sec_in_hour * 24  # 86400 sec


interval = int(input('Введите размер интервала в секундах: '))
if interval < 60:
    print(interval, 'секунд')

elif (interval < sec_in_hour) and (interval > sec_in_min) :
    min = interval // sec_in_min
    sec = interval - min * sec_in_min
    print(min, 'минут', sec, 'секунд')

elif (interval < sec_in_day) and (interval > sec_in_hour)  :
    hour = interval // sec_in_hour
    min = (interval - hour * sec_in_hour) // sec_in_min
    sec = interval - hour * sec_in_hour - min * sec_in_min
    print(hour, 'час', min, 'минут', sec, 'секунд')

elif interval > sec_in_day:
    day = interval // sec_in_day
    hour = (interval - day * sec_in_day) // sec_in_hour
    min = (interval - day * sec_in_day - hour * sec_in_hour) // sec_in_min
    sec = interval - day * sec_in_day - hour * sec_in_hour - min * sec_in_min
    print(day, 'дней', hour, 'час', min, 'минут', sec, 'секунд')
