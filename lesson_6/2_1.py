from collections import Counter

def pars_string(str):
    indx = str.find(' ')
    str1 = str[:indx]
    return (str1)

log = open("nginx_logs.txt", 'r', encoding="utf-8")
mass = []

while True:
    line = log.readline()
    if not line:
        break
    mass.append(pars_string(line))

serch_set = list(set(mass))


ip_addr = ''
ip_count = 0

for i in range(len(serch_set) - 1):
    temp = mass.count(serch_set[i])
    if temp > ip_count:
        ip_addr = serch_set[i]
        ip_count = mass.count(serch_set[i])

print("Адресс спамера ",ip_addr," количество запросов ", ip_count)