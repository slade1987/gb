import sys
#Вариант1

hobby = input("Введите путь к файлу с хобби")
hobby = hobby.replace("\\","\\\\")
hobby = open(hobby, 'r', encoding="utf-8")

users = input("Введите путь к файлу с ФИО")
users = users.replace("\\","\\\\")
users = open(users, 'r', encoding="utf-8")

res = input("Введите путь для сохранения")
res = res.replace("\\","\\\\")
res = open(res, 'a', encoding="utf-8")

mass = []

while True:
    str_hobby = hobby.readline()
    user = users.readline().replace("\n","")
    if not user and not str_hobby:
        break
    elif not user:
        exit(1)
    elif not str_hobby:
        f, n, p = user.split(",")
        mass.append(((f,n,p),None))
    else:
        f, n, p = user.split(",")
        mass.append(((f,n,p), str_hobby.replace("\n","")))


#print(str(dict(mass)))
#Для вывода в файл расскоментировать
res.write(str(dict(mass)))


hobby.close()
users.close()
res.close()



#Вариант 2
'''
hobby = open(sys.argv[1], 'r', encoding="utf-8")
users = open(sys.argv[2], 'r', encoding="utf-8")
res = open(sys.argv[3], 'a', encoding="utf-8")

mass = []

while True:
    str_hobby = hobby.readline()
    user = users.readline().replace("\n","")
    if not user and not str_hobby:
        break
    elif not user:
        exit(1)
    elif not str_hobby:
        f, n, p = user.split(",")
        mass.append(((f,n,p),None))
    else:
        f, n, p = user.split(",")
        mass.append(((f,n,p), str_hobby.replace("\n","")))

print(str(dict(mass)))
#Для вывода в файл расскоментировать
#res.write(str(dict(mass)))


hobby.close()
users.close()
res.close()
'''
