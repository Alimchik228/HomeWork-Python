with open('text5.txt', 'w+') as file_obj:
    content ='4 5 6 7 8 9'
    file_obj.write(content)
    file_obj.seek(0)
    p = file_obj.read()
    print(p)
sum = 0
for i in (0, len(p), 2):
    sum += int(p[i])
    print(sum)

print(sum)
print(len(p))