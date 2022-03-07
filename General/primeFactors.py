inputVal = int(input("Enter integer >= 2: "))

# initialise factor to 2
factor = 2

while factor <= inputVal:
    # check if input is divisible by factor
    if inputVal % factor == 0:
        inputVal = inputVal // factor
        # conclude factor is a prime number
        print(factor)
    else:
        # increment factor by 1
        factor += 1
    
