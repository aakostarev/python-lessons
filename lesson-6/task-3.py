# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position
# (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера
# на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage_val, bonus_val):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage_val, 'bonus': bonus_val}

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя работника: {self.name} {self.surname}.')
    def get_total_income(self):
        total = sum(self._income.values())
        print(f'Доход с учетом премии равен: {total}')

worker_1 = Position("Alex", "Ivanov", "driver", 45000, 20000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.position)
print(worker_1._income)