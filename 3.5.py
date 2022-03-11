k = ''
summa = 0
while '*' not in k:
    k = input()
    count = sum([int(i) for i in k.split() if i.isdigit()])
    summa += count
    print(summa)