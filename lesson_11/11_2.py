class MyError(Exception):
    def __init__(self,text):
        self.text = text

a = int(input("Введите делимое"))
try:
    b = int(input("Введите делитель"))
    if b == 0:
        raise MyError("Message")
    print(a/b)
except MyError:
    print("На ноль делить нельзя")
