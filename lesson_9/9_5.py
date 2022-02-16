class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        pass

class Pen(Stationery):
    def draw(self):
        print(f'Это рисование {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Это рисование карандашем')

class Handler(Stationery):
    def draw(self):
        print(f'Новый метод рисования {self.title}')

pen = Pen("Pen")
pen.draw()

pencil = Pencil("Pencil")
pencil.draw()

handler = Handler("Handler")
handler.draw()