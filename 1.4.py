class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return 'Машина поехала'
    def stop(self):
        return 'Машина остановилась'
    def turn(self, direction):
        return (f'Машина повернула {direction}')
    def showspeed(self):
        return self.speed

class TownCar(Car):
    def showspeed(self):
        if self.speed > 60:
            return 'Превышение скорости'
        else:
            return self.speed


class SportCar(Car):
    pass

class WorkCar(Car):
    def showspeed(self):
        if self.speed > 40:
            return 'Превышение скорости'
        else:
            return self.speed


class PoliceCar(Car):
    pass


Lamborgini = SportCar(200, 'yellow', 'Lamborgini', True)
Toyota = WorkCar(55, 'green', 'Toyota', False)
print(Lamborgini.turn('left'))
print(Lamborgini.showspeed())
print(Toyota.showspeed())




