class Cell:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return self.number + other.number
    def __sub__(self, other):
        if self.number < other.number:
            return 'Число ячеек первой клетки меньше чем второй'
        else:
            return self.number - other.number
    def __mul__(self, other):
        return self.number * other.number
    def __truediv__(self, other):
        return self.number//other.number
    def make_order(self, kol):
        s = ''
        for i in range(self.number//kol):
            s += '*'*kol + '\n'
        s += self.number % kol*'*' +'\n'
        return s

cell_1 = Cell(20)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(3))



