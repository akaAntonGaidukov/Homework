# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"New car: {self.name} (color {self.color}) police car - {self.is_police}")

    def go(self):
        print(f"{self.name}: Car is going. ")

    def stop(self):
        print(f"{self.name}: Car stopped. ")

    def turn(self, direction):
        print(f"{self.name}: Car is turning {'left' if direction == 0 else 'right'}. ")

    def show_speed(self):
        print(f"{self.name}: Car`s speed: {self.speed}. ")

class TownCar(Car):

    def show_speed(self):
        return f"{self.name}: Car`s speed: {self.speed}. Speeding!" if self.speed > 60 else f"{self.name}: Car`s speed: {self.speed}. "

class WorkCar(Car):

    def show_speed(self):
        return f"{self.name}: Car`s speed: {self.speed}. Speeding!" if self.speed > 40 else f"{self.name}: Car`s speed: {self.speed}. "

class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('LADA', 'White', 110)
police_car.go()
police_car.show_speed()
police_car.turn(0)
police_car.turn(0)
police_car.stop()
print()


work_car = WorkCar('Peugeot', 'Yellow', 60)
work_car.go()
work_car.turn(0)
print(work_car.show_speed())
work_car.turn(1)
work_car.stop()
print()

sport_car = SportCar('Lexus', 'Red', 160)
sport_car.go()
sport_car.turn(0)
sport_car.show_speed()
sport_car.turn(1)
sport_car.stop()
print()

town_car = TownCar('Mercedes', 'Grey', 78)
town_car.go()
town_car.turn(1)
print(town_car.show_speed())
town_car.turn(1)
town_car.stop()

