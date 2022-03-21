class Compex_number():

    def __init__(self,complex_string):
        temp = complex_string.find("+")
        self.a = complex_string[:temp]
        self.b = complex_string[temp + 1:complex_string.find("j")]

    def __add__(self, other):
        str_compa = int(self.a) + int(other.a)
        str_compj = str(int(self.b) + int(other.b)) + 'j'
        res = str(str_compa) + "+" + str_compj
        print(res)
        return res

    def __mul__(self, other):
        res = int(self.a) * int(other.a) - int(self.b) * int(other.b)
        res = str(res) + "+" + (str(int(self.b) * int(other.a) + int(self.a) * int(other.b)) + "j")
        print(res)
        return res

b = Compex_number('4+5j')
c = Compex_number('2+5j')
s = b + c
ss = b * c

