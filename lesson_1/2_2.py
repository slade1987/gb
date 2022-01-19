list = []
res_list = []
res_summ = 0
temp = 0
i = 1
j = 0
while (i < 1000):
    summ = 0
    list.append(i ** 3 + 17)
    temp = list[j]
    temp_list = []
    while (temp > 0):
        temp_list.append(temp % 10)
        temp //= 10
    for num in temp_list:
        summ = summ + num
    if (summ % 7 == 0):
        res_list.append(summ)
        res_summ = res_summ + list[j]
    i += 2
    j += 1
print("Список кубов " + str(list))
print("Количество элемнтов " + str(len(list)))
print("Список элементов полученных / на 7 " + str(res_list))
print("Итоговая сумма " + str(res_summ))
