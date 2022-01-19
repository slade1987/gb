i = 0
while (i < 101):
    if (((i % 10) == 0) or ((i % 10) > 4) or ((i > 10) and (i < 20))):
        print(str(i) + " Процентов")
    elif ((i % 10) == 1):
        print(str(i) + " Процент")
    else:
        print(str(i) + " Процента")
    i += 1
