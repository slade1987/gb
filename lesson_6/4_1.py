hobby = open("hobby.csv", 'r', encoding="utf-8")
users = open("users.csv", 'r', encoding="utf-8")
res = open("3_1_res.txt", 'a', encoding="utf-8")

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
