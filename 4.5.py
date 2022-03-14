from functools import reduce
def p(k):
    count = 100
    while count < k:
      if count % 2 == 0:
        yield count
      count += 1
k = 1001
my_gen = p(k)
list_1 = []
for el in my_gen:
    list_1.append(el)
print(list_1)
list_1 = reduce(lambda a,b: a*b, list_1)
print(list_1)