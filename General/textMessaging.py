import re

path = 'D://Documents//UoL//COMP517_Programming_Fundamentals//week_4//'

countLine = 1
keysDict = {}
posDict = {}

# open the text file with keys information
with open(path+'text_keys.txt', 'r') as f:
    content = f.readlines()
    # read each line and append it to dictionary
    for line in content:
        line = re.sub('\n', '', line)
        line = line.split()
        if line[1] == 'space':
            keysDict[' '] = 0
            posDict[' '] = 0
        else:
            for i in range(0, len(line[1])):
                keysDict[line[1][i]] = countLine
                posDict[line[1][i]] = i+1
        countLine += 1

# obtain input
inputString = input("Enter text: ")

output = []
for char in inputString:
    # map input to keys combination
    key = keysDict.get(char.upper())
    pos = posDict.get(char.upper())
    if key == 0:
        output.append(str(0))
    for i in range(pos):
        output.append(str(key))

print("Keys combination for '{}' is {}".format(inputString, ''.join(output)))
