import re

path = 'D://Documents//UoL//COMP517_Programming_Fundamentals//week_4//'

morseCodeDict = {}
with open(path+'morse_code.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        line = re.sub('\n', '', line).strip()
        line = line.split()
        morseCodeDict[line[0]] = line[1]

inputString = input("Enter text: ")

output = []
for char in inputString:
    morse_code = morseCodeDict.get(char.upper())
    output.append(morse_code)

print("Morse Code for '{}' is {}".format(inputString, ''.join(output)))

