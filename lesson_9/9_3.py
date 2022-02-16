class Worker():
    def __init__(self, name, sername, position, wage, bonus):
        self.n = name
        self.s = sername
        self.p = position
        self._i = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.n + ' ' + self.s
        return full_name
    def get_total_imcome(self):
        total_incom = self._i['profit'] + self._i['bonus']
        return total_incom

pos = Position("Ivan","Paranych","Engeneer",500,400)

print(pos.get_full_name())
print(pos.get_total_imcome())