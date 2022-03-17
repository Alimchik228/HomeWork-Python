with open('text2.txt', 'r') as file_obj:
    content = file_obj.readlines()
    print(content)
print(f'Кол. строк в файле: {len(content)}')

p=[]
for i in range(len(content)):
    p.extend(content[i].split())

print(f'Кол. слов в файле: {len(p)}')