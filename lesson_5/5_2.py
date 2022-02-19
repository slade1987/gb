n = int(input("Введите число"))
#Решение 1
#num = [print(i) for i in range(n) if i % 2 > 0]
#Решение 2
num = [i for i in range(n + 1) if i % 2 > 0]
print(num)