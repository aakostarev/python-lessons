# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
#
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class MyDate:
    def __init__(self, date):
        self.date = date

    @classmethod
    def changing (cls, strng):
        integ = []
        i = 0
        while i < len(strng):
            s_int = ''
            a = strng[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < len(strng):
                    a = strng[i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
        if cls.validation(integ):
            return f'число: {integ[0]}, месяц: {integ[1]}, год: {integ[2]}'
        else:
            return ('Ошибка валидации')

    @staticmethod
    def validation(date):
        day = date[0]
        month = date[1]
        year = date[2]
        print(f'Валидация {date}, as a day: {day}, as a month: {month}, as a year: {year}')
        if (day < 1) or (day > 31):
            print ('День не валиден!')
            return False
        if (month < 1) or (month > 12):
            print ('Месяц не валиден!')
            return False
        if (year < 1900) or (year > 2050):
            print ('Год не валиден!')
            return False
        else:
            return True
a = MyDate.changing('dg454f67b4e5c3gf676')
print(a)
print ('*' * 40)
b = MyDate.changing('dg12f02b1988e5c3gf676')
print(b)


