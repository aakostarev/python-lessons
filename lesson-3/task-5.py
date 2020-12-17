# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.
import time
str_list = input('Введите строку чисел, разделенных пробелом. Если хотите выйти, включите символ "q" в строку: ').split()
start = time.perf_counter()
# так как во вводе могут быть десятичные числа, то пишем функцию проверки на вхождение точки:
def str_to_num(str) -> object:
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():
        return int(str)
    elif 'q' in str:
        return ('q')

# в этой же функции далее заполняем числами список num_list:
num_list = []
sum = 0
for i in str_list:
    n = str_to_num(i)
    if n is not (None or 'q'):
        num_list.append(n)
        sum += n
    elif n == 'q':
        break
print(num_list) # проверка корректности обработки введенных данных
print(f'Сумма по строке: {sum}')
tmp_list = input('Хотите добавить числа в строку?. Если хотите выйти, включите символ "q" в строку: ').split()
str_list += tmp_list
print(f'Дополненная строка: {str_list}')

time_used = time.perf_counter() - start #служебный код
print(f'{time_used:.5f}' ' sec') #служебный код