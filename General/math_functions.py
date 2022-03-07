import math

print()
print("Operations")
print("==================")
print()
print("Cosine of a number: 1")
print("Sine of a number: 2")
print("Tangent of a number: 3")
print("Squareroot of a number: 4")
print("Natural logarithm of a number: 5")
print("Base-10 logarithm of a number: 6")
print("Base-2 logarithm of a number: 7")
print("Factorial of a number: 8")
print("Round a number: 9")
print("Product of a number: 10")
print("Enter q to exit")
print()


# function to get two inputs
def getTwoInputs():
    inputVal1 = int(input("Enter Value 1: " ))
    inputVal2 = int(input("Enter Value 2: " ))
    return inputVal1, inputVal2

# function to get one input
def getOneInputs():
    inputVal1 = input("Enter Value 1: " )
    return inputVal1

# function to return cosine of a number
def cos(x):
    return math.cos(x)

# function to return sine of a number
def sin(x):
    return math.cos(x)

# function to return tangent of a number
def tan(x):
    return math.tan(x)

# function to return squareroot of a number
def sqrt(x):
    return math.sqrt(x)

# function to return natural logarithm of a number
def log(x):
    return math.log(x)

# function to return base-10 logarithm of a number
def log_10(x):
    return math.log10(x)

# function to return base-2 logarithm of a number
def log_2(x):
    return math.log2(x)

# function to return factorial of a number
def fact(x):
    return math.factorial(x)

# function to round a number to the nearest integer
def round(x):
    return math.floor(x)

# function to return product of a sequence
def prod(userList):
    return math.prod(userList)



inputVal = input("Select operation: " )

if inputVal == 'q':
    exit()
elif int(inputVal) == 1:
    inputVal1 = int(getOneInputs())
    print("Cosine of a number: ", math.sum(inputVal1))
    #print("Cosine of a number: ", cos(inputVal1))
elif int(inputVal) == 2:
    inputVal1 = int(getOneInputs())
    print("Cosine of a number: ", sin(inputVal1))
elif int(inputVal) == 3:
    inputVal1 = int(getOneInputs())
    print("Tangent of a number: ", tan(inputVal1))
elif int(inputVal) == 4:
    inputVal1 = int(getOneInputs())
    print("Tangent of a number: ", sqrt(inputVal1))    
elif int(inputVal) == 4:
    inputVal1 = int(getOneInputs())
    print("Squareroot of a number: ", sqrt(inputVal1))   
elif int(inputVal) == 5:
    inputVal1 = int(getOneInputs())
    print("Natural logarithm of a number: ", log(inputVal1))   
elif int(inputVal) == 6:
    inputVal1 = int(getOneInputs())
    print("Base-10 logarithm of a number: ", log_10(inputVal1))   
elif int(inputVal) == 7:
    inputVal1 = int(getOneInputs())
    print("Base-2 logarithm of a number: ", log_2(inputVal1))   
elif int(inputVal) == 8:
    inputVal1 = int(getOneInputs())
    print("Factorial of a number: ", fact(inputVal1))   
elif int(inputVal) == 9:
    inputVal1 = float(getOneInputs())
    print("Rounding the number: ", round(inputVal1))   
elif int(inputVal) == 10:
    inputString = input("Enter a list elements separated by space: ")
    userList = inputString.split()
    userList = [int(num) for num in userList]
    product = prod(userList)
    print("The product of number list: ", product)

  
print()
