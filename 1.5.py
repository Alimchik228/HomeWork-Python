class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return 'Запуск отприсовки'

class Pen(Stationery):
    def draw(self):
        return 'Запуск надписи'

class Pensil(Stationery):
    def draw(self):
        return 'Запуск чертежа'

class Handle(Stationery):
    def draw(self):
        return 'Запуск выделения'


pen = Pen('pen')
print(pen.draw())
pensil = Pensil('pensil')
print(pensil.draw())
handle = Handle('Handle')
print(handle.draw())

