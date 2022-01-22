str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(str)):
    if (str[i].isdigit()):
        str[i] = '"' + str[i] + '"'
    elif (str[i][0] == '+'):
        str[i] = '"' + str[i] + '"'
print(" ".join(str))
