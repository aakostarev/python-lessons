# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
#
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен
# контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа
# и строки. При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число. Класс-исключение
# должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.
class IntInputError(Exception):
    def __init__(self, txt):
        self.txt = txt

print('Вводите элементы списка (строка либо число) через enter')
print(' Для окончания ввода элементов списка введите "stop"')
rices = []
a = ''
while a != 'stop':
    try:
        a = input('-->> ')
        if (not a.isdigit()) and (a != 'stop'):
            raise IntInputError('Не числа в список ввода не попадают. Введите число или "stop" '
                                'для выхода.')
    except IntInputError as err:
        print(err)
    else:
        if a != 'stop':
            rices.append(a)
print(rices)