nums = {
    'one': 'один',
    'two': 'два',
    'three':'три',
    'four':'четыре',
}


with open('text4.txt', 'r') as file_obj, open('text_test.txt','w') as file:
    file_lines = file_obj.readlines()
    print(file_lines)
    for line in file_lines:
        data = line.split()
        rus_num = nums.get(data[0])
        file.write(f'{line.replace(data[0], rus_num)}')





