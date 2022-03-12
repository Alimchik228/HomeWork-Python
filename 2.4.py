k = ''
k = input()
p=0

for i in range(len(k.split())):
     p+=1
     print('Номер строки:', ' ', end='')
     print(p, ' ', end='')
     print(k[0:10])