from abc import ABC, abstractmethod
class Cloth(ABC):
    @abstractmethod
    def raschet(self):
        pass

class Coat(Cloth):
    def __init__(self,V):
        self.v = V

    def raschet(self):
        return round((self.v/6.5 + 0.5),3)


class Costume(Cloth):
    def __init__(self,H):
        self.h = H
    def raschet(self):
        return round((2 * self.h + 0.3),3)

my_coat = Coat(10)
print(my_coat.raschet())

my_costume = Costume(4)
print(my_costume.raschet())