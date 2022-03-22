class Matrix:
    def __init__(self, list_obj):
        self.list_obj = list_obj

    def __str__(self):
        s = ''
        for i in range(len(self.list_obj)):
            for j in range(len(self.list_obj[i])):
                s += f'{self.list_obj[i][j]:3}'
            s += '\n'
        return s
    def __add__(self, other):
        for i in range(len(self.list_obj)):
            for j in range(len(self.list_obj[i])):
                self.list_obj[i][j] += other.list_obj[i][j]
        return self




matr_1 = Matrix([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
matr_2 = Matrix([ [4, 5, 6], [4, 5, 6], [7, 8, 9] ])

print(matr_1 + matr_2)