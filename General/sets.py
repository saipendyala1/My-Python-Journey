""" # Set is a data structure which is a collection of
# unordered elements, unique elements, unindexed elements
# order of data is not important, however need unique elements


# # create set
a = {1, 2, 3, 4}
print(a)


b = [1, 2, 3, 4, 4, 5, 5]
c = set(a)
print(c)


# s = {} # creates dictionary
s = set()
print(s)


# set operations
# 1. get length of a set
exampleSet = {1, 2, 3, 4}
print(len(exampleSet))
print()

# access set elements
exampleSet = {1, 2, 3, 4}
#exampleSet[0]
for term in exampleSet:
    print(term)
print()

# add elments to a set
# add or update method
# add one element to the set
exampleSet = {1, 2, 3, 4}
exampleSet.add(4)
print(exampleSet)
print()


# add mulitple elements to the set
exampleSet = {1, 2, 3, 4}

# update set
exampleSet1 = {1, 2, 3, 4, 5, 6}
exampleSet.update(exampleSet1)
print(exampleSet)


# update list
exampleSet1 = [1, 2, 3, 4, 5, 6]
exampleSet.update(exampleSet1)
print(exampleSet)


# # remove and discard
exampleSet = {1, 2, 3, 4, 5, 6}
exampleSet.remove(4)
print(exampleSet)

#exampleSet.remove(4)
#print(exampleSet)

exampleSet.discard(4)
print(exampleSet)

exampleSet.clear()
print(exampleSet)


# intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

print()
# intersection 
# get elements that are in both sets
s4 = s1.intersection(s2)
print(s4)
s5 = s1.intersection(s2, s3)
print(s5)
s5 = s1 & s3
print(s5)

# intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

print()
# difference
# get elements that are in s1 and not in s2
s4 = s1.difference(s2)
print(s4)
s4 = s1 - s2
print(s4)
# get elements that are in s2 and not in s1
s4 = s2.difference(s1)
print(s4)

# s5 = s1.difference(s2, s3)
# print(s5)


# intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

print()
# symmetric difference
s4 = s1.difference(s2)
print(s4)
s4 = s1.symmetric_difference(s2)
print(s4)
 """



import re

shoes = set()
belts = set()
shirts = set()

path = 'D://Documents//UoL//COMP517_Programming_Fundamentals//week_4//'

with open(path+'sample-sales.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    for line in content:
        line = re.sub('\n', '', line)
        split_line = line.split(',')

        customer = split_line[0]+' '+split_line[1]
        category = split_line[3]
        
        if category == 'Shoes':
            shoes.add(customer)
        if category == "Belt":
            belts.add(customer)
        if category == "Shirt":
            shirts.add(customer)

f.close()


print("{} customers purchased shoes".format(len(shoes)))
print("{} customers purchased belts".format(len(belts)))
print("{} customers purchased shirts".format(len(shirts)))

# Intersection of A and B is a set of elements that are common in both sets
print("{} customers have purchased shoes and belts".format(len(shoes & belts)))
#print("{} customers have purchased shoes and belts".format(len(shoes.intersection(belts))))
print("{} customers have purchased shoes and shirts".format(len(shoes & shirts)))

# Difference
print("{} customers have purchased shoes but not belts".format(len(shoes - belts)))
#print("{} customers have purchased shoes but not belts".format(len(shoes.difference(belts))))

print("{} customers have purchased shoes, belts and shirts".format(len(shoes & belts & shirts)))

print()
for customer in shoes & belts & shirts:
    print(customer)

