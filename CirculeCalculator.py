# Circle Calculator
# Main Menu
print("=================")
print("Enter")
print("=================")
print("1 To calculate diameter (d),circumference (C) and area (A)")
print("2 To calculate diameter (d), area (A) and radius (r)")
print("3 To calculate diameter (d), radius (r) and circumference (C)")
print("q To exit")
print()

# Assign the value of pi as global
global pi
pi = 3.14

# This function Calculates the diameter (d),circumference (C) and area (A) of a circle
def calculate_d_C_A():
    # Take input from the user
    radius = float(input("Enter the Radius Of the Circle in Centimetres: "))

    # Calculate the diameter(d),circumference (C) and area (A)
    diameter = 2 * radius
    circumference = 2 * pi * radius
    area = pi * (radius ** 2)

    # OUTPUT: display the diameter(d),circumference (C) and area (A)
    print("The Diameter Of the Circle in Centimetres: {0:.2f}".format(diameter))
    print("The Circumference Of the Circle in Centimetres: {0:.2f}".format(circumference))
    print("The Area Of the Circle in Centimetres: {0:.2f} ".format(area))

# This  function Calculates the diameter (d), area (A) and radius (r) of a circle
def calculate_d_A_r():
    # Take input from the user
    circumference = float(input("Enter the Circumference Of the Circle in Centimetres: "))

    # Calculate the diameter (d), area (A) and radius (r)
    diameter = circumference / pi
    area = (circumference ** 2) / 4 * pi
    radius = circumference / 2 * pi

    #OUTPUT: Display diameter (d), area (A) and radius (r)
    print("The Diameter Of the Circle in Centimetres: {0:.2f}".format(diameter))
    print("The Area Of the Circle in Centimetres: {0:.2f}".format(area))
    print("The radius Of the Circle in Centimetres: {0:.2f} ".format(radius))

# This function calculates the diameter (d), radius (r) and circumference (C) of a circle
def calculate_r_C_d():
    # Take input from the user
    area = float(input("Enter the Area Of the Circle in Centimetres: "))

    # calculate the diameter (d), radius (r) and circumference (C)
    radius = (area / pi) ** 0.5
    circumference = (2 * pi)*((area / pi)** 0.5)
    diameter = 2 *((area / pi) ** 0.5)

    # OUTPUT : Display diameter (d), radius (r) and circumference (C)
    print("The radius Of the Circle in Centimetres: {0:.2f} ".format(radius))
    print("The circumference Of the Circle in Centimetres: {0:.2f}".format(circumference))
    print("The diameter Of the Circle in Centimetres: {0:.2f} ".format(diameter))


while True:
    # Take input from the user
    choice = input("Enter your Choice(1/2/3/q): ")

    # check if the choice is one of four options
    if choice in ('1','2','3','q'):

        # Quit the program if "q" is entered
        if (choice == 'q'):
            # exit the program
            exit()
        elif (choice == '1'):
            calculate_d_C_A()
        elif (choice == '2'):
            calculate_d_A_r()
        elif (choice == '3'):
            calculate_r_C_d()
        break
    else:
        print("Please Enter the valid input!")

