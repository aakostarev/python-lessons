# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(a, b):
    try:
        a, b = float(a), float(b)
        c = round(a / b, 4)
    except ZeroDivisionError:
        return('Деление на 0!')
    except ValueError:
        return ('Value error')
    return(c)
d, e = (i for i in input('Введите 2 числа через пробел: ').split())
print (f'Результат деления: {division(d, e)}') if type(division(d, e)) != str else print (division(d, e))

