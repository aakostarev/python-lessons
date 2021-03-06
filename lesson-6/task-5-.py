# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три
# дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title='Принадлежности для письма'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}.')

class Pen (Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой.')

class Pencil (Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} карандашом.')

class Marker (Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} маркером.')

x = Stationery()
x.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()