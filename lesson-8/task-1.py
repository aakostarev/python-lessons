# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
#
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class Data:

    @classmethod
    def changing (cls, strng):
        global integ
        s = strng
        integ = []
        i = 0
        while i < len(s):
            s_int = ''
            a = s[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < len(s):
                    a = s[i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))

    @staticmethod
    def validation(integ):
        day = integ[0]
        month = integ[1]
        year = integ[2]
        print(f'Валидация {integ}, as a day: {day}, as a month: {month}, as a year: {year}')
        if (day < 1) or (day > 31):
            print ('День не валиден!')
        if (month < 1) or (month > 12):
            print ('Месяц не валиден!')
        if (year < 1900) or (year > 2050):
            print ('Год не валиден!')
Data.changing('dg454f67b4e5c3gf676')
Data.validation(integ)
print ('*' * 40)
Data.changing('dg12f02b1988e5c3gf676')
Data.validation(integ)
print('Bye!')

