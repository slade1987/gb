str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
mas = []

for i in range(len(str)):
    if (str[i].isdigit()):
        mas.append(i)
        if (int(str[i]) < 9):
            str[i] = '0' + str[i]
    elif (str[i][0] == '+'):
        mas.append(i)
        c,n = str[i].split("+")
        if (int(n) < 9):
            str[i] = '+' + '0' + n
mas.reverse()

for i in mas:
    str.insert(i + 1,'"')
    str.insert(i,'"')
print(" ".join(str))
