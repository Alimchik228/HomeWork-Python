list = []
k = ''
k = input()
list = [int(i)  for i in k.split() ]
p = 0
print(list)
for i in range(0, len(list)-1, 2):
    if i+1 <= len(list):
        p = list[i]
        list[i] = list[i+1]
        list[i+1] = p
print(list)