with open('text3.txt', 'r') as file_obj:
    content = file_obj.readlines()
    print(content)
p = []
for i in range(len(content)):
    p.extend(content[i].split())
print(p)
k = 0
sum = 0
for i in range(1, len(p), 2):
    if int(p[i]) < 20000:
        print(p[i-1])
        k = k + 1
        sum = sum + int(p[i])
print(f'Средняя заработная плата сотрудников: {sum / k}')