# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого
# типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

class Storehouse:
    def __init__(self):
        self._dict = {}

    def reception(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def transfer(self, model):
        if self._dict[model]:
            self._dict.setdefault(model).pop(0)

class Equipment:
    def __init__(self, inv_number, model, color, quantity, *args):
        self.inv_number = inv_number
        self.model = model
        self.color = color
        self.group = self.__class__.__name__
        self.quantity = quantity

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'Model: {self.model}, inv_number: {self.inv_number}, color:{self.color}, ' \
               f'quantity: {self.quantity}'

class Printer(Equipment):
    def __init__(self, inv_number, model, color, quantity, print_speed):
        super().__init__(inv_number, model, color, quantity)

        self.print_speed = print_speed

class Scaner(Equipment):
    def __init__(self, inv_number, model, color, quantity, scan_resolution):
        super().__init__(inv_number, model, color, quantity)
        self.scan_resolution = scan_resolution

class Xerox(Equipment):
    def __init__(self, inv_number, model, color, quantity, copy_speed):
        super().__init__(inv_number, model, color, quantity)
        self.copy_speed = copy_speed

storehouse =Storehouse() #создаем склад
hp1022 = Printer(12,'Hewlett-Packard LaserJet 1022', 'white', 2, '10 pages/min')
storehouse.reception(hp1022) # принимаем на склад
canonLx9 = Scaner(10, 'Canon CanoScan Lx9', 'grey', 5, '1200 dpi')
storehouse.reception(canonLx9)
xeroxML1200 = Xerox(11, 'Xerox ML1200', 'black', 10, '15 pages/min')
storehouse.reception(xeroxML1200)
print(f'Инвентаризация склада 1:\n{storehouse._dict}')
storehouse.transfer('Scaner')
print(f'Инвентаризация склада 2:\n{storehouse._dict}')
