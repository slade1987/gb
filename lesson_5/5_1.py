def odd_num(num):
    for i in range(num + 1):
        if (i % 2) > 0:
            yield i

print(*odd_num(int(input("Введите число"))))