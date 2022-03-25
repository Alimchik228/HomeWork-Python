class complex:

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f'{self.real} + i*{self.image}'

    def __add__(self, other):
        return complex(self.real + other.real, self.image + other.image)


c_1 = complex(2, 5)
c_2 = complex(5, 2)
print(c_1)
print(c_1 + c_2)
