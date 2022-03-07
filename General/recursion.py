# Recursion
# ---------
# A recursive solution in a programming language such as Python is one in which a
# function calls itself one or more times in order to solve a particular problem.

n = 5
inputnum = n

factorial = 1
while(n>0):
    factorial = factorial*n
    n = n-1

print("Factorial of {} is {}".format(inputnum, factorial))


def factorial(n):
    if n == 1: # The termination condition
        return 1 # The base case
    else:
        res = n * factorial(n-1) # The recursive call
        return res
    
print(factorial(5)) 