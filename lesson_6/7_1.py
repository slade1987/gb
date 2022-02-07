from sys import argv

sale_doc = open("sale1.txt",'r+',encoding="utf-8")
#Вариант 1
'''
num_str = input("Введите номер позиции")
sale_doc.seek((int(num_str) - 1) * 6)
res = sale_doc.readline()
res = res.replace('.','')
res = res.replace('\n','')
if not res.isnumeric() :
    print("Вы ввели несуществующий номер позиции")
    exit(1)
num_pr = input("Введите данные - пять знаков")
sale_doc.seek((int(num_str) - 1) * 6)
sale_doc.write(num_pr)

'''
#Вариант 2

res = sale_doc.seek((int(argv[1]) - 1) * 6)
res = sale_doc.readline()
res = res.replace('.','')
res = res.replace('\n','')
if not res.isnumeric() :
    print("Вы ввели несуществующий номер позиции")
    exit(1)
sale_doc.seek((int(argv[1]) - 1) * 6)
sale_doc.write(argv[2])

sale_doc.close()

