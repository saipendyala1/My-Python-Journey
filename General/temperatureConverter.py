tempList = []
tempList.append(("degrees Celsius", "degrees Fahrenheit"))

for i in range(0,100):
    if i % 10 == 0:
        tempList.append((i, (i*9/5)+32))

for term in tempList:
    print("{:>25}{:>25}".format(term[0], term[1]))


