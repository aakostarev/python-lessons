# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
numb = 0
max = 0
a = int(input('Введите целое положительное число: '))
while a <= 0:
    a = int(input('Неверно, введите целое положительное число: '))
while a // 10 != 0:
    numb = a % 10
    if numb >= max:
        max = numb
    a = a // 10
if (a //10 == 0) and (a % 10 > max):
    max = a % 10
print(f'Самая большая цифра в числе равна {max}')

