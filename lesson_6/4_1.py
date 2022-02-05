hobby = open("hobby.csv", 'r', encoding="utf-8")
users = open("users.csv", 'r', encoding="utf-8")
res = open("3_1_res.txt", 'a', encoding="utf-8")



mass = []
while True:
    str_hobby = hobby.readline()
    user = users.readline().replace("\n","")
    f, n, p = user.split(",")
    if not users.readline() and not str_hobby:
        break
    elif not users.readline():
        exit(1)
    elif not str_hobby:
        mass.append(((f,n,p),None))
    else:
        mass.append(((f,n,p), str_hobby.replace("\n","")))

print((str(dict(mass))))

