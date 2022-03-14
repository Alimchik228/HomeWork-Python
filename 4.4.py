list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_2 = []
def find(k):
    i = 0
    while i != len(list_1):
        p = True
        for j in range(i+1, len(list_1)):
            if list_1[i] == list_1[j]:
                p = False
        for j in range(0, i):
            if list_1[i] == list_1[j]:
                p = False


        if p != False:
            yield list_1[i]
        i += 1

my_gen = find(list_1)
for el in my_gen:
  list_2.append(el)
print(list_2)






