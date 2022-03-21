from time import sleep

class TrafficLight:
    colors = ('red', 'yellow', 'green')
    delay = (5, 2, 4)
    def __init__(self):
        self.__color = 'green'

    def running(self):
        for i in self.colors:
            self.__color = i
            print(self.__color)
            sleep(self.delay[self.colors.index(self.__color)])
traffic_light = TrafficLight()
traffic_light.running()


