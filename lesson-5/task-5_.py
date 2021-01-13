# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def my_func(string):
    try:
        count = 0
        string = map (int, string)
        for digit in string:
            count += digit
        return count
    except ValueError:
        return ('Введите только числа!')

with open ('task-5.txt', 'w+', encoding='utf-8') as out_f:
    out_f.write(input ('Введите набор чисел, разделенных пробелами: '))
    out_f.seek(0)
    my_string = out_f.readline().split()
    print('Сумма чисел в файле равна:', my_func(my_string))
