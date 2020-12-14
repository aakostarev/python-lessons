# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#решение с помощью списка. Можно было бы все числа от 1 до 12
#включить в один список и сравнивать введенное число с диапазонами из списка
# но тогда зачем нам вообще список
winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if month in winter:
    print(f'{month}-й месяц относится к зиме')
elif month in spring:
    print(f'{month}-й месяц относится к весне')
elif month in summer:
    print(f'{month}-й месяц относится к лету')
elif month in autumn:
    print(f'{month}-й месяц относится к осени')
else:
    print('Вы ввели неверное значение месяца')

#решение с помощью словаря:
year = {}
year['winter'] = [12,1,2]
year['spring'] = [3,4,5]
year['summer'] = [6,7,8]
year['autumn'] = [9,10,11]
for i in range (3):
    if year['winter'][i] == month:
        print(f'{month}-й месяц относится к зиме')
    elif year['spring'][i] == month:
        print(f'{month}-й месяц относится к весне')
    elif year['summer'][i] == month:
        print(f'{month}-й месяц относится к лету')
    elif year['autumn'][i] == month:
        print(f'{month}-й месяц относится к осени')