class Cell:
    def __init__(self,cell_number):
        self.cellnuber = cell_number

    def __add__(self, other):
        return str(self.cellnuber + other.cellnuber)

    def __sub__(self, other):
        if self.cellnuber < other.cellnuber:
            return "ОШИБКА"
        else:
            return str(self.cellnuber - other.cellnuber)

    def __mul__(self, other):
        return str(self.cellnuber * other.cellnuber)

    def __truediv__(self, other):
        if other.cellnuber < 1:
            return "Ошибка клеток не может быть меньше одной"
        elif self.cellnuber < other.cellnuber:
            return "Будет ноль клеток, что невозможно"
        else:
            return str(self.cellnuber // other.cellnuber)

    def make_order(self,numb):
        return str(self.cellnuber * numb)

a = Cell(5)
a.make_order(5)

