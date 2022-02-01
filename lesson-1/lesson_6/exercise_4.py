__author__ = 'Болотов Андрей Вячеславович'
"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, name, color):
        self.speed = 0
        self.is_police = False
        self.name = name
        self._color = color

    def go(self, speed_up):
        self.speed += speed_up

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        print(f'Автомобиль {self.name} поверул на {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 60:
            print(f'Вы превысили скорость  на {self.speed - 60} км. в час')


class SportCar(Car):
    def max_speed(self):
        print(f'Максимальная скорасть {self.name} 300 км. в час')


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 40:
            print(f'Вы превысили скорость  на {self.speed - 40} км. в час')


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


if __name__ == '__main__':
    car_1 = SportCar('Audi', 'Red')
    car_2 = TownCar('Oka', 'White')
    car_3 = WorkCar('Lada', 'Rose')
    car_4 = PoliceCar('Ford', 'Blue')
    print('Начальное состояние автомобилей')
    print(f'1 - {car_1.name, car_1.speed, car_1._color, car_1.is_police}')
    print(f'1 - {car_2.name, car_2.speed, car_2._color, car_2.is_police}')
    print(f'1 - {car_3.name, car_3.speed, car_3._color, car_3.is_police}')
    print(f'1 - {car_4.name, car_4.speed, car_4._color, car_4.is_police}')
    car_1.go(50)
    car_1.turn('лево')
    car_1.go(50)
    car_1.show_speed()
    car_1.max_speed()
    car_2.go(80)
    car_2.show_speed()
    car_2.stop()
    car_3.go(30)
    car_3.show_speed()
    car_3.turn('право')
    car_3.go(20)
    car_3.show_speed()
    car_3.stop()
    car_4.go(60)
    car_4.show_speed()
    print('Конечное состояние автомобилей')
    print(f'1 - {car_1.name, car_1.speed, car_1._color, car_1.is_police}')
    print(f'1 - {car_2.name, car_2.speed, car_2._color, car_2.is_police}')
    print(f'1 - {car_3.name, car_3.speed, car_3._color, car_3.is_police}')
    print(f'1 - {car_4.name, car_4.speed, car_4._color, car_4.is_police}')
