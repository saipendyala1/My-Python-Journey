print()

print("=============")
print("Enter:")
print("=============")

print("1 for main")
print("2 for dessert")
print("3 for both")
print("4 for none")
print()


# function to check input
def get_input(guest_num):

    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:

        try:
            val = int(input("Guest " + str(guest_num) + ", Enter your input: " ))

        # If wrong input is provided
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! You have entered an incorrect input. Please enter again.")
            print()

        # When proper input is obtained,
        # the loop will end.
        else:
            if val == 1 or val == 2 or val == 3 or val == 4:
                print("Thank you Guest " + str(guest_num) + " for your input.")
                print()
                break
            else:
                print("You have entered an invalid input, please enter correct input")
                
    return val

# initialise counters
counter_main = 0
counter_dessert = 0

guests_list = [1, 2, 3]
guestDict = {}

for guest_num in guests_list:

    guest_choice = get_input(guest_num)

    if guest_choice == 1:
        counter_main +=1
        guestDict["Guest " + str(guest_num)] = "1 main"
    elif guest_choice == 2:
        counter_dessert +=1
        guestDict["Guest " + str(guest_num)] = "1 dessert"
    elif guest_choice == 3:
        counter_main += 1
        counter_dessert += 1
        guestDict["Guest "+ str(guest_num)] = "1 main, 1 dessert"
    elif guest_choice == 4:
        guestDict["Guest "+ str(guest_num)] = "0 main, 0 dessert"

print()
print("==================")


print("Total mains requried: ", counter_main)
print("Total desserts requried: ", counter_dessert)

print()
for key, value in guestDict.items():
    print(key + " : " + value)

print("==================")


