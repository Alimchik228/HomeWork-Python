def SumMax(num_1, num_2, num_3):
  list = [num_1, num_2, num_3]
  max_1 = max(list)
  num_max_1 = list.index(max_1)
  del(list[num_max_1])
  max_2 = max(list)
  num_max_2 = list.index(max_2)
  return max_2 + max_1

print("Введите 3 числа")
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(f"Наибольшая сумма = {SumMax(num_1, num_2, num_3)} ")