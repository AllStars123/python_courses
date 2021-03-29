# Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError,
# если что-то не так, например:
#
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

def dec_with_arg(arg_of_dec):
    def val_checker(func):
        def check(*args):
            if arg_of_dec(*args):
                res = func(*args)
                print(res)
            else:
                raise ValueError(f"wrong val{args}")
            return res
        return check
    return val_checker


@dec_with_arg(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

calc_cube(-7)

