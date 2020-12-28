# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
string = input('Введите строку: ')

#способ решения 1
def int_func(str):
    new_list = [element.capitalize() for element in str.split()]
    new_str = ' '.join(new_list)
    return new_str
print(int_func(string))

#способ решения 2
print(string.title())
