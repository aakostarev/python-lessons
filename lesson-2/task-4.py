# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
string = input ('Введите строку из нескольких слов, разделённых пробелами: ')
split_string = string.split()
print(split_string)
for i in range (len(split_string)):
       print(i+1, ' ',split_string[i] [0:10])