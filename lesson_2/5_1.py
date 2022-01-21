prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
prices.sort()
result = []
for i in range(len(prices)):
    temp = str(prices[i]).split('.')
    if (len(temp) > 1):
        if (len(temp[1]) > 1):
            result.append(temp[0] + " руб " + str(temp[1]) + " коп" )
        else:
            result.append(temp[0] + " руб " + str(temp[1]) + '0' + " коп")
    else:
        result.append(temp[0] + " руб ")

print("id = ",id(result),result)
result.reverse()
print("id = ",id(result),result)

print("Самые дорогие товары")
for i in range(0, 5):
    print(result[i])

