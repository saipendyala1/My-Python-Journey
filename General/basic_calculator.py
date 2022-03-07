print()
print("Operations")
print("==================")
print()
print("Addition: 1")
print("Subtraction: 2")
print("Multiplication: 3")
print("Division: 4")
print("Division with rounded value: 5")
print("Exponent: 6")
print("Enter q to exit")
print()


def getTwoInputs():
    inputVal1 = int(input("Enter Value 1: " ))
    inputVal2 = int(input("Enter Value 2: " ))
    return inputVal1, inputVal2

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x, y):
    return x/y

def divRound(x,y):
    return x//y

def exp(x,y):
    return x**y
    

inputVal = input("Select operation: " )

if inputVal == 'q':
    exit()
elif int(inputVal) == 1:
    inputVal1, inputVal2 = getTwoInputs()
    print("Addition: ", add(inputVal1, inputVal2))
elif int(inputVal) == 2:
    inputVal1, inputVal2 = getTwoInputs()
    print("Subtraction: ", sub(inputVal1, inputVal2))
elif int(inputVal) == 3:
    inputVal1, inputVal2 = getTwoInputs()
    print("Product: ", mult(inputVal1, inputVal2))
elif int(inputVal) == 4:
    inputVal1, inputVal2 = getTwoInputs()
    print("Division: ", div(inputVal1, inputVal2))
elif int(inputVal) == 5:
    inputVal1, inputVal2 = getTwoInputs()
    print("Division with rounded valued: ", divRound(inputVal1, inputVal2))
elif int(inputVal) == 6:
    inputVal1, inputVal2 = getTwoInputs()
    print("Exponent: ", exp(inputVal1, inputVal2))
    
    