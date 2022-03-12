n = int(input())
list = []

info_2 = {
        'название':[],
        'цена':[],
        'количество':[],
        'ед':[],
    }

for i in range(0,n):

    print('Введите через пробел название, цену, количество, единицы: ')
    info = {'название': '',
             'цена': '',
            'количество': '',
            'единицы': '',
    }
    info_1 = input()
    info_1 = info_1.split()
    info['название'] = info_1[0]
    info['цена'] = info_1[1]
    info['количество'] = info_1[2]
    info['единицы'] = info_1[3]
    # list.append([])
    # list[i].append(i + 1)
    # list[i].append(info)
    # list[i]=tuple(list[i])

    list.append((i+1, info))
    print(list[i])


    info_2['название'].append(info_1[0])
    info_2['цена'].append(info_1[1])
    info_2['количество'].append(info_1[2])
    info_2['ед'].append(info_1[3])
    print(info_2)