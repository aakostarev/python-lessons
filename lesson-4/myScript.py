def zarplata ():
    while True:
        try:
            s1 = float(input('Введите значение выработки в часах: '))
            s2 = float(input('Введите объем отработанных часов: '))
            s3 = float(input('Введите размер премии: '))
            if not (s1, s2, s3 >=0):
                print('Вы ввели некорректные данные')
            else:
                print('Данные введены верно. Возвращаем расчет.')
                break
        except ValueError:
            print('Все 3 значения должны быть числовыми.')
    return s1 * s2 + s3