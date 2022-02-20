class Cell:
    def __init__(self,cell_number):
        self.cellnuber = cell_number

    def __add__(self, other):
        return Cell(self.cellnuber + other.cellnuber)

    def __sub__(self, other):
        if self.cellnuber < other.cellnuber:
            return "ОШИБКА"
        else:
            return Cell(self.cellnuber - other.cellnuber)

    def __mul__(self, other):
        return Cell(self.cellnuber * other.cellnuber)

    def __truediv__(self, other):
        if other.cellnuber < 1:
            return "Ошибка клеток не может быть меньше одной"
        elif self.cellnuber < other.cellnuber:
            return "Будет ноль клеток, что невозможно"
        else:
            return Cell(self.cellnuber // other.cellnuber)

    def make_order(self,numb):
        cell_str = ''
        i = 0
        if self.cellnuber > numb:
            i = self.cellnuber // numb
        else:
            cell_str = numb * '*'
            return cell_str
        for j in range(i):
            cell_str = cell_str + (numb * '*')
            cell_str = cell_str + '\n'

        if (self.cellnuber % numb ) > 0:
            cell_str = cell_str + ((self.cellnuber % numb) * '*')
        return cell_str


a = Cell(12)
b = Cell(10)
print('a - b',a - b)
print('a + b',a + b)
print('a * b',a * b)
print('a / b',a / b)
print('\n \nГрафическое отображение ')
print(a.make_order(5))

