dic = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре","Five":"Пять","Six":"Шесть","Seven":"Семь","Eight":"Восемь","Nine":"Девят","Ten":"Десять","Zero":"Ноль"}

def num_translate(word,b=True):
    word = word.title()
    if not b:
        return dic.get(word).lower()
    return dic.get(word)

word = input("Введите ключ")

if (not word.istitle()):
    print(num_translate(word,False))
else:
    print(num_translate(word))