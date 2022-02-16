def pars_string(str):
    indx = str.find(' ')
    str1 = str[:indx]
    indx = str.find('"') + 1
    str2 = str[indx: indx + 3]
    indx1 = str.find(' ', indx + 4)
    str3 = str[indx + 4: indx1]

    return (str1, str2, str3)


log = open("nginx_logs.txt", 'r', encoding="utf-8")
mass = []

''' Вариант 1
for i in log:
    mass.append(pars_string(i))
log.close()
print(mass[1])
'''
# Вариант 2
while True:
    line = log.readline()
    if not line:
        break
    mass.append(pars_string(line))

print(mass[1])
