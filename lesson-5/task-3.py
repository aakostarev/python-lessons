# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

out_f = open("task-3.txt", "r")

def is_number(s) -> object:
    try:
        float(s)
        return True
    except ValueError:
        return False

total = 0
print('Фамилии сотрудников с окладом менее 20 тысяч: ')
while True:
    content = out_f.read(1024).split()
    for element in content:
        if not is_number(element):
            word = element
        elif is_number(element):
            digit = float(element)
            total += digit
            if digit <= 20000:
                print(word)

    if not content:
        break
out_f.seek(0)
count = sum( 1 for line in out_f )
print(total, count)
print(f'Средняя зарплата равна: {round(total / count, 2)}')
out_f.close()