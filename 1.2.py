class Road:
    lenght = 0
    width = 0

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def weight(self, kg, depth):
        return self._width * self._lenght * kg * depth /1000

road_1 = Road(5000, 20)
print(road_1.weight(25, 5))

