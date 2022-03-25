class MyException(Exception):

    def __init__(self, value):
        self.value = value

print('Введите числа')
n = input()

if not n.isdigit():
    raise MyException('Вводите только числа!')