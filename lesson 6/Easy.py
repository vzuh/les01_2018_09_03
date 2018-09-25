# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# class TownCar:
#     def __init__(self, speed, color, name, police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = police
#
#     def go(self):
#         print('go')
#
#     def stop(self):
#         print('stop')
#
#     def turn(self, direction):
#         print('turn {}'.format(direction))
#
#
# class SportCar:
#     def __init__(self, speed, color, name, police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = police
#
#     def go(self):
#         print('go')
#
#     def stop(self):
#         print('stop')
#
#     def turn(self, direction):
#         print('turn {}'.format(direction))
#
#
# class WorkCar:
#     def __init__(self, speed, color, name, police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = police
#
#     def go(self):
#         print('go')
#
#     def stop(self):
#         print('stop')
#
#     def turn(self, direction):
#         print('turn {}'.format(direction))
#
#
# class PoliceCar:
#     def __init__(self, speed, color, name, police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = police
#
#     def go(self):
#         print('go')
#
#     def stop(self):
#         print('stop')
#
#     def turn(self, direction):
#         print('turn {}'.format(direction))

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print('turn {}'.format(direction))


class TownCar(Car):
    def __init__(self):
        super().__init__()


class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = True


class SportCar(Car):
    def __init__(self):
        super().__init__()


class WorkCar(Car):
    def __init__(self):
        super().__init__()
