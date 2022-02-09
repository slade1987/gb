def thesaurus(*fio):
    dic = {}
    for i in fio:
        if i[0][0] in dic:
            dic[i[0][0]] = dic[i[0]] + [i]
        else:
            dic[i[0][0]] = [i]

    return dic

result = thesaurus("Иван", "Мария", "Петр", "Илья","Ира","Галя","Иосиф")
print(result)

