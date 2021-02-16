# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_zeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input('Введите делимое число: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise My_zeroDivError('Попытка деления на 0!')
except My_zeroDivError as err:
    print (err)
else:
    print (f'Результат - {a/b}')
finally:
    print('Программа завершена.')