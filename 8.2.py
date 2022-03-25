class MyException(Exception):

    def __init__(self, value):
        self.value = value
print('Введите числитель: ')
n = int(input())
print('Введите знаменатель: ')

m = int(input())
if m == 0:
    raise MyException('Делить на ноль нельзя!')