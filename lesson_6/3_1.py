
hobby = open("hobby.csv", 'r', encoding="utf-8")
users = open("users.csv", 'r', encoding="utf-8")
res = open("3_1_res.txt", 'a', encoding="utf-8")



#Решение 1
mass = []
while True:
    str_user = users.readline()
    str_hobby = hobby.readline()

    if not str_user and not str_hobby:
        break
    elif not str_user:
        exit(1)
    elif not str_hobby:
        mass.append((str_user.replace("\n",""),None))
    else:
        mass.append((str_user.replace("\n",""), str_hobby.replace("\n","")))

res.write(str(dict(mass)))


'''
#Решение 2
while True:
    str_user = users.readline()
    str_hobby = hobby.readline()
    mass = []
    if not str_user and not str_hobby:
        break
    elif not str_user:
        exit(1)
    elif not str_hobby:
        mass.append((str_user.replace("\n",""),None))
    else:
        mass.append((str_user.replace("\n",""), str_hobby.replace("\n","")))
    res.write(str(dict(mass)))
    res.write("\n")

'''
