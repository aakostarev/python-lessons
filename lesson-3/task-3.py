# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        d = a + b + c - min(a,b,c)
        return d
    except ValueError:
        return ('Введите только числа!')

a1,b1, c1 = (i for i in input('Введите числа a, b, c через пробел: ').split())
print (f'Сумма наибольших двух аргументов равна: {my_func(a1,b1,c1)}')