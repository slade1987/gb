from sys import argv

sale = open("sale.txt", 'a', encoding="utf-8")
string = str(argv[1]) + '\n'
sale.write(string)
sale.close()