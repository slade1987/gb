dic = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре","Five":"Пять","Six":"Шесть","Seven":"Семь","Eight":"Восемь","Nine":"Девят","Ten":"Десять","Zero":"Ноль"}

def num_translate(word):
    return dic.get(word,"None")

word = input("Введите ключ")
print(num_translate(word))