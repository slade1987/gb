str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(str)):
    if (str[i].isdigit()):
        if(int(str[i]) > 9 ):
            str[i] = '"' + str[i] + '"'
        else:
            str[i] = '"' +'0' + str[i] + '"'
    elif (str[i][0] == '+'):
        c,n = str[i].split('+')
        if (int(n) < 9 ):
            str[i] = '"' +'+' + '0' + n + '"'
        else:
            str[i] = '"' +'+' + n +'"'
print(" ".join(str))
