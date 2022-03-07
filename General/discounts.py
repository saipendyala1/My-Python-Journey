

inputString = input("Enter price of products: ")

inputList = inputString.split()
inputList = [float(num) for num in inputList]

#print(inputList)

j = 0
while j < len(inputList):
    originalPrice = inputList[j]
    discountAmount = 60 * originalPrice / 100.00
    newPrice = originalPrice - discountAmount
    print()
    print("Product "+str(j+1))

    print("Original price: ", originalPrice)
    print("Discount (60%): ", discountAmount)
    print("New price: ", round(newPrice, 2))
    

    j = j+1



""" # Calls for an infinite loop that keeps executing
while True:

    val = input("Enter price or 'q' to exit: " )
    if val == 'q':
        exit()
    else:
        originalPrice = float(val)
        discountAmount = 60 * originalPrice / 100.00
        newPrice = originalPrice - discountAmount

        print("Original price: ", originalPrice)
        print("Discount (60%): ", discountAmount)
        print("New price: ", round(newPrice, 2))
        print()
 """
