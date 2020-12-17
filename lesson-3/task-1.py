# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        c = 'Деление на 0!'
        return(c)
d, e = (float(i) for i in input('Введите 2 числа через пробел: ').split())
print (f'Результат деления: {division(d, e):.2f}') if type(division(d, e)) != str else print (division(d, e))

