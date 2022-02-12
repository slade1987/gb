src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 344,]
j = len(src) - 1
i = 0
while i < len(src):
    j = len(src) - 1
    tmp = ''
    while j > i:
        if src[i] == src[j]:
            src.pop(j)
            tmp = src[i]
        j -= 1
    if tmp != '':
        src.remove(src[i])
        i -= 1
    i += 1

print(src)
