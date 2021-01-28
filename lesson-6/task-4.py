# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__ (self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Марка машины: {self.name}, цвет: {self.color}, это полиция: {self.is_police}.')

    def go(self):
        print(f'{self.name} поехал(а)')

    def stop(self):
        print(f'{self.name} остановился(лась)')

    def turn(self, direction):
        if direction == 0:
            print(f'{self.name} повернул(а) налево')
        else:
            print(f'{self.name} повернул(а) направо')

    def show_speed(self):
        return f'{self.name} - скорость автомобиля: {self.speed}.'

class TownCar(Car): #городской автомобиль

    def show_speed(self):
        return f'{self.name} - скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f'{self.name} - скорость автомобиля: {self.speed}.'

class WorkCar(Car): #грузовой автомобиль

    def show_speed(self):
        return f'{self.name} - скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'{self.name} - скорость автомобиля: {self.speed}.'

class SportCar(Car): #грузовой автомобиль

    def show_speed(self): #спортивный автомобиль
        return f'{self.name} - скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 90 else f'{self.name} - скорость автомобиля: {self.speed}.'

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police = True):
        super().__init__(name, color, speed, is_police)

town_car = TownCar(61, 'синяя', 'Городская машина')
town_car.go()
print(town_car.show_speed())
town_car.turn(1)
town_car.stop()
print()

work_car = WorkCar(30, 'оранжевый', 'Самосвал')
work_car.go()
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()
