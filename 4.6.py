from itertools import cycle
list_1 = [2, 4, 6, 8]
my_gen = cycle(list_1)
count = 0
print('Генератор cycle: ')
for el in my_gen:
    print(el)
    count += 1
    if count > 7:
        break
print(' ')
print('Генератор count: ')
from itertools import count
my_obj = count(3, 1)
i = 0
for el in my_obj:
    print(el)
    i += 1
    if i > 10:
        break

