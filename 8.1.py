class Data:
    __date = ''
    def __init__(self, date):
        Data.__date = date

    def print(self):
       return self.__date

    @classmethod
    def get_int(cls):
        d = []
        d = [int(i) for i in cls.__date.split() if i.isdigit()]
        return d

    @staticmethod
    def proverka(d):
        if d[0] < 1 or d[0] > 31:
          return False
        if d[1] < 1 or d[1] > 12:
            return False
        if d[2] < 1 or d[2] > 2022:
            return False
        return True

date = Data('02 - 12 - 2001')
date_1 = Data('34 - 11 - 2001')
print(date_1.proverka(date_1.get_int()))
print(date.print())
print(date.get_int())
print(date.proverka(date.get_int()))