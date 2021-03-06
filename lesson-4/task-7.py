# Имя файла : task-7.py
# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
def fact(x):
    res = 1
    for i in range(x):
        res = res * (i + 1)
    yield res

try:
    n = int(input('Введите целое число n: '))
    for j in range (1, n + 1):
        print(f'Факториал {j} : {[j for j in fact(j)]}')
except ValueError:
    print('Вы ввели не целочисленное значение n!')