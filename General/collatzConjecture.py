def collatz_sequence(x):
    seq = [x]
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1 
        seq.append(x)    # Added line
    return seq

while True:
    inputVal = input("Enter integer: ")
    try:
        if int(inputVal) > 0:
            seq = collatz_sequence(int(inputVal))
            print(seq)
        else:
            exit()
    except ValueError:
        print("Please enter an integer")

