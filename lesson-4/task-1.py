from sys import argv
def zarplata ():
        try:
            s1, s2, s3 = map(float, argv[1:])
            print(f'Данные введены верно. Расчет: {s1 * s2 + s3}')
        except ValueError:
            print('Все 3 значения должны быть числовыми.')

zarplata()