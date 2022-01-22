str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
mas = []

for i in range(len(str)):
    if (str[i].isdigit()):
        mas.append(i)
    elif (str[i][0] == '+'):
        mas.append(i)
mas.reverse()

for i in mas:
    str.insert(i + 1,'"')
    str.insert(i,'"')
print(" ".join(str))
