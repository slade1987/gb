class MyError(Exception):
    def __init__(self,text):
        self.text = text

p = ''
mas = []
while True:
    try:
        p = input("Ввидете p")
        if p == 'stop':
            print(mas)
            break
        if not int(p.isdigit()):
            raise MyError("Error")
        mas.append(int(p))
    except MyError:
        print("error")
