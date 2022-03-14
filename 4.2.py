list_1 = [2, 3, 9, 1, 3, 5, 5]
list_2 = []
# for i in range(len(list_1)-1):
#     if list_1[i+1] > list_1[i]:
#         list_2.append(list_1[i+1])
# print(list_2)
list_2 = [list_1[i+1] for i in range(len(list_1)-1) if list_1[i+1]>list_1[i]]
print(list_2)



