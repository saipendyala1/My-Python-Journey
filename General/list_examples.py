# list operations

## list.append(x)
## Add an item to the end of the list. Equivalent to a[len(a):] = [x].
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits)
# fruits.append('mango')
# print(fruits)

## list.extend(iterable)
## Extend the list by appending all the items from the iterable.
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits1 = ['mango', 'water melon', 'pineapple']
# print(fruits)
# fruits.extend(fruits1)
# print(fruits)


## list.insert(i, x)
## Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits)
# fruits.insert(0, 'mango')
# print(fruits)


## list.remove(x)
## Remove the first item from the list whose value is equal to x. 
# # It raises a ValueError if there is no such item.
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits)
# fruits.remove('kiwi')
# print(fruits)

## list.pop([i])
## Remove the item at the given position in the list, and return it. 
## If no index is specified, a.pop() removes and returns the last item in the list. 
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits)
# popItem = fruits.pop(0)
# print(popItem)
# print(fruits)

## delete element from a list using del keyword
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits)
# del fruits[0]
# print(fruits)

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# del fruits[-1]
# print(fruits)


## list.sort(*, key=None, reverse=False)
## Sort the items of the list in place 
## (the arguments can be used for sort customization,).
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.sort()
# print(fruits)
# print()

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# sortedList = sorted(fruits)
# print(sortedList)
# print()

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.sort(reverse=True)
# print(fruits)


# # using key for sorting the list
# # take second element for sort
# def takeSecond(elem):
#     print(elem)
#     return elem[1]

# itemsList = [[2, 2], [3, 4], [4, 1], [1, 3]]

# # sort list with key
# itemsList.sort(key=takeSecond)
# # print list
# print('Sorted list:', itemsList)


# using key for sorting the list
# take second element for sort
# itemsList = [[2, 2, 4, 5], [3, 4], [4, 1, 4], [1, 3, 5, 6, 7]]

# # sort list with key
# itemsList.sort(key=len)
# # print list
# print('Sorted list:', itemsList)


# print()
# # sort list with key
# itemsList.sort(key=len, reverse=True)
# # print list
# print('Sorted list:', itemsList)


# ## list slicing
# ## a[start:stop:step]
# ## a[start:stop]  # items start through stop-1
# ## a[start:]      # items start through the rest of the array
# ## a[:stop]       # items from the beginning through stop-1
# ## a[:]           # a copy of the whole array
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[1:4])
# print(a[1:])
# print(a[:4])
# print(a[:])
# print()


# ## a[-1]    # last item in the array
# ## a[-2:]   # last two items in the array
# ## a[:-2]   # everything except the last two items
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[-1])
# print(a[-2:])
# print(a[:-2])
# print()


# ## a[start:stop:step]
# ## return every other element in the list
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[::2])
# print()


# ## Return every 2nd item between position 2 to 7
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[2:7:2])
# print()


# ## Negative steps
# ## Return every 2nd item between position 6 to 1
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[6:1:-2])


## randomly select elements from list
## Python has a built-in module that you can use to make random numbers.
## The random module has a set of methods:
## https://docs.python.org/3/library/random.html
# import random

## random.randint(a, b) returns a random integer between a and b inclusive.
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# random_index = random.randint(0,len(letters)-1)
# print(letters[random_index])
# print()

# for item in letters:
#     random_index = random.randint(0,len(letters)-1)
#     print(letters[random_index])


## random.randrange(a) is another method which returns a random number n such that 0 <= n < a:
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# random_index = random.randrange(len(letters))

# print(letters[random_index])


## random.choice() is another choice precicely designed to solve this problem:
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(random.choice(letters))


## selecting more than one element
## selects elements without replacement, i.e., 
## it selects without duplicates and repetitions.
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(random.sample(letters, 3))


## random.choices is another function to return list of 
## randomly selected elements from a given iterable
## can return duplicates
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(random.choices(letters, k=3))

## TUPLES

# ## Tuples are identical to lists in all respects, except for the following properties:
# ## Tuples are defined by enclosing the elements in 
# ## parentheses (()) instead of square brackets ([]).

# ## Lists are mutable while tuples are not mutable
# ## mutable implies python object of this type can be modified
# ## Lists
# a = [0, 1, 2, 3]
# print(a)
# a[0] = 1
# print(a)

# ## Tuples
# a = (0, 1, 2, 3)
# print(a)
# a[0] = 1
# print(a)


# a = [0, 1, 2, 3]
# print(id(a))
# a[0] = -1
# print(id(a))
# print()

# a = (0, 1, 2, 3)
# print(id(a))
# a = (-1, 1, 2, 3)
# print(id(a))


# a_list = []
# for i in range(0, 4):
#     a_list.append(i)
#     print(a_list)
#     print(id(a_list))

# a_tuple = ()
# for i in range(0, 4):
#     a_tuple = a_tuple + (i,)
#     print(a_tuple)
#     print(id(a_tuple))


# ## indexing and slicing in tuples
# t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
# print(t[0])
# print(t[-1])
# print(t[1::2])


# ## tuple packing and unpacking
# b = ("Bob", 19, "CS")    # tuple packing
# print(b)
# (name, age, studies) = b    # tuple unpacking
# print(name)
# print(age)
# print(studies)
