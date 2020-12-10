sec = int(input('Введите время в секундах: '))
time_hours = sec // 3600
time_min = (sec - time_hours * 3600) // 60
time_sec = sec - time_hours * 3600 - time_min * 60
print(f'Это {time_hours} час(ов), {time_min} минут(а) и {time_sec} секунд(а)')