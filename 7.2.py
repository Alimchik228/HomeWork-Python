from abc import ABC, abstractmethod



class Clothes(ABC):
    @abstractmethod
    def tissue(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def tissue(self):
        return self.v/6.5 + 0.5

class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def tissue(self):
        return self.h/2 + 0.3

coat = Coat(20)
costume = Costume(20)
print(coat.tissue)


print(costume.tissue)

print(coat.tissue + costume.tissue)



