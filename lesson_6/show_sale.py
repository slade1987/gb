import sys
from sys import argv
from itertools import islice

sale_doc = open("sale.txt",'r',encoding="utf-8")

if len(argv) == 1:
    for i in sale_doc:
        print(i,end='')
elif len(argv) == 2:
    sls1 = list(islice(sale_doc,int(argv[1]),sys.maxsize))
    for i in sls1:
        print(i,end="")
elif len(argv) == 3:
    sls1 = list(islice(sale_doc, int(argv[1]), int(argv[2])))
    for i in sls1:
        print(i, end="")
else:
    print("Что то пошло не так (((")

sale_doc.close()
