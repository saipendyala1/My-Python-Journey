# Exceptions vs Syntax Errors

# Syntax errors occur when the parser detects 
# an incorrect statement
# print(0/0)

# Exception error occurs whenever syntactically correct 
# Python code results in an error (runtime errors).

print(10 * (1/0))
# ZeroDivisionError: division by zero

print(4 + spam*3)
# NameError: name 'spam' is not defined

print('2' + 2)
# TypeError: Can't convert 'int' object to str implicitly


# syntax of try....except...else blocks

# try:
#    You do your operations here;
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block. 


# AssertionError Exeception
# Instead of allowing the program to crash midway,
# we can make an assertion in Python.
# We assert that a certain condition is met.
# If the condition is True, then continue. 
# If False, the program throws an AssertionError exception.

'''
import sys
## assert ('linux' in sys.platform), "This code runs on Linux only."

# assert keyword is used when debugging code.
# assert keyword lets you test if a condition in
# your code returns True, if not, 
# the program will raise an AssertionError.
# You can write a message to be written 
# if the code returns False, check the example below.


# try and except block - is used to catch 
# and handle exceptions in Python.

# use try block to write the code that might throw an error
# when error occurs, the control of the program 
# jumps to except block and continues
# if exception does not occur, the except block is skipped

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except:
    pass
print()
# we handled the error by simply using pass

# include exception to generate more
# meaningful message
try:
    linux_interaction()
except:
    print('Linux function was not executed')
print()


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')
print()


# Example 2
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
print()

# catch FileNotFoundError
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
print()


# multiple exceptions
try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')
print()

# try-except-else
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')
print()


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')

'''