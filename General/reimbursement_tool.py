
employeeName = input("Enter Name: " )
jobTitle = input("Enter Job Title: " )
dateOfTravel = input("Date of travel: " )
startMileage = input("Enter start mileage: " )
endMileage = input("Enter end mileage: " )
hotelCost = input("Enter hotel cost: " )
foodCost = input("Enter food cost: " )
publicTranscost = input("Enter public transport cost: " )

billsChecked = True


if billsChecked:
    cost = 0
    print(employeeName)

    foodCost = (100 * int(foodCost)) / 100.00
    cost = cost + foodCost

    milesCost = (int(endMileage) - int(startMileage)) * 0.43
    cost = cost+milesCost

    hotelCost = (100 * int(hotelCost)) / 100.00
    cost = cost + hotelCost

    publicTranscost = (100 * int(publicTranscost)) / 100.00
    cost = cost + publicTranscost

    print("Amoung payable to " + employeeName + " is: " + str(cost))

