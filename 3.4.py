def degree(x, y):
    for i in range(1,y):
      x = x*x
    return x
print("Введите два числа: ")
x = int(input())
y = int(input())
print(f'x в степени y = {1/degree(x, y)}')