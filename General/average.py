# a = list(map(int, input("\nEnter the numbers : ").strip().split()))
# print(a)

print("Enter list of values. Use 0 to indicate the end of list")
print()

inputString = input("Enter values: ")

inputList = inputString.split()
inputList = [int(num) for num in inputList]

# check if 0 is in the list
if 0 in inputList:
    print(inputList)

    # check the index of 0
    index_0 = inputList.index(0)
    if index_0 == 0:
        print("Unable to calculate average")
        print("Please enter correct values")
        exit()
    
    elif index_0 < len(inputList)-1:
        print(index_0)
        inputListNew = []
        for i in range(0, index_0):
            inputListNew.append(inputList[i])
        inputList = inputListNew
        
    elif index_0 ==  len(inputList)-1:
        del inputList[-1]

print('inputList: ', inputList)
totalSum = 0
for num in inputList:
    totalSum = totalSum + num

average = totalSum / len(inputList)

print()
print('average: ', average)


