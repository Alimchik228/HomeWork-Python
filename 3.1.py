def degree(num_1, num_2):
    if num_2 != 0:
      return num_1 / num_2
    else:
        print("Делить на ноль нельзя!")

print ("Введите числитель: ")
num_1 = int(input())
print ("Введите знаменатель: ")
num_2 = int(input())
print("Деление = ", " ",degree(num_1, num_2))