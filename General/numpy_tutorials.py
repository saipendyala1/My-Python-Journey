# NumPy
# =============
# fast and efficient ways of creating arrays
# manipulating numerical data inside them. 
# Lists - heterogeneous content, Numpy array - homogeneous
# NumPy arrays are faster and more compact than Python lists
# consumes less memory and convenient to use. 
# better optimization

# array is a central data structure of the NumPy library. 
# a grid of values with information about the raw data
# the elements are all of the same type - dtype.
# rank of the array is the number of dimensions.
# shape of the array is a tuple of integers - size of the array along each dimension.

# initialie arrays with Python Lists
import numpy as np 

# convert lists into arrays
L = [1, 2, 3, 4, 5, 6]
print(L)
A = np.array(L)
print(A)
print()

# nested list
L = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(L)
A = np.array(L)
print(A)
print()

print(type(A)) # Prints "<class 'numpy.ndarray'>"


# shape of the array
print()
print('shape of the array')
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
print()

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a.shape)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
print(a)
print(a.shape)
print()


# some terminology
# ndarray - “N-dimensional array.” - array with any number of dimensions.
# 1-D, or one-dimensional array, 2-D, or two-dimensional array,
# The NumPy ndarray class is used to represent both matrices and vectors. 
# vector - an array with a single dimension (there’s no difference between row and column vectors)
# matrix - an array with two dimensions. 
# tensor - 3-D or higher dimensional arrays


# axes - in NumPy, dimensions are called axes. 
# a 2-D array has 2 axes
# vertical axis (axis 0) and horizontal axis (axis 1)
a = np.array([[0., 0., 0.],
              [1., 1., 1.]])
print(a)
print()

# create basic array
a = np.array([1, 2, 3])
print(a)
print()

# arrays filled with zeros
a = np.zeros(4)
print(a)
print()

# arrays filled with ones
a = np.ones(4)
print(a)
print()

# empty array
a = np.empty(2)
print(a)
print()
# empty creates an array whose initial content is random 
# empty over zeros or ones - speed, fill every element afterwards


# array with a range of elements
a = np.arange(4)
print(a)
print()


# array with spaced intervals. 
# (first number, last number, step size)
a = np.arange(2, 9, 2) # array([2, 4, 6, 8])
print(a)
print()


# dtype - default floating point (np.float64)
# specify required data type using the dtype keyword.

x = np.ones(2)
print(x)
x = np.ones(2, dtype=np.int64)
print(x)
print()



# shape and size of an array
a = np.array([[[0, 1, 2, 3],
               [4, 5, 6, 7]],
              [[0, 1, 2, 3],
               [4, 5, 6, 7]],
              [[0 ,1 ,2, 3],
               [4, 5, 6, 7]]])

# d1 = ['w1', 'w2]
# d1 = ['w3', 'w4]
# d1 = ['w0', 'w2]

# ndarray.ndim - number of axes, or dimensions
print('ndim or axes:', a.ndim)
print()

# ndarray.size - total number of elements
# product of the elements of the array’s shape.
print('size:', a.size)
print()

# ndarray.shape - tuple of integers that indicate the number of elements
# stored along each dimension of the array.
print('shape:', a.shape)
print()


# reshaping an array
# arr.reshape() - new shape to an array without changing the data.
# when reshape method, the array you want to produce needs to have 
# the same number of elements as the original array. 
# Example - array with 12 elements - new array also has a total of 12 elements

print('reshape')
a = np.arange(6)
print(a)
print()

b = a.reshape(3, 2)
print(b)
print()

print('convert 1-D to 2-D')
# convert 1D array into a 2D array - add a new axis to an array
# np.newaxis increases  dimensions of an array by one dimension when used once.
# 1D array ==> 2D array; 2D array ==> 3D array, and so on.
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape) # (6,)
print(a)
print()

# use np.newaxis to add a new axis
a2 = a[np.newaxis, :]
print(a2.shape) # (1, 6)
print(a2)
print()

# to get column vector, insert axis along the second dimension:
a2 = a[:, np.newaxis]
print(a2.shape) # (6, 1)
print(a2)
print()

print('np.expand_dims')
# expand an array by inserting a new axis 
# at a specified position with np.expand_dims.
b = np.expand_dims(a, axis=1)
print(b.shape) # (6, 1)
print()

b = np.expand_dims(a, axis=0)
print(b.shape) # (1, 6)
print()


# index and slice NumPy arrays - similar to to Python lists.
print('indexing and slicing')
data = np.array([1, 2, 3])

print(data[1]) # 2
print(data[0:2]) # array([1, 2])
print(data[1:]) # array([2, 3])
print(data[-2:]) # array([2, 3])
print()


L = [[1,2], [3,4]]
print('L: ', L)
print()

# get value at row 0 and column 1
print(L[0][1])
print()

A = np.array(L)
print(A)
print()

print(A[0][1])
print()

print(A[0,1])
print()

# get column
print(A[:,1])
print()

# Transpose
print(A.T)
print()

# exponential 
print(np.exp(A))
print()

# we can also pass a list
print(np.exp(L))
print()



# 2-D array
a = np.zeros((2, 3))
print(a)
print()
#array([[0., 0., 0.],
#       [0., 0., 0.]])

a = np.zeros((2, 3, 2))
print(a)
print()
#array([[[0., 0.],
#        [0., 0.],
#        [0., 0.]],
#       [[0., 0.],
#        [0., 0.],
#        [0., 0.]]])



#Creates an array of 4 x 4 with the main diagonal of 1
print('np.identity')
a = np.identity(3)
print(a)
print(a.shape)
print()
#array([[1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.]])

print('np.eye')
a = np.eye(3)
print(a)
print(a.shape)
print()
#array([[1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.]])


a = np.eye(3, 5)
print(a)
print()
#array([[1., 0., 0., 0., 0.],
#       [0., 1., 0., 0., 0.],
#       [0., 0., 1., 0., 0.]])
#or you can change the diagonal position


a = np.eye(3,5,k=1)
print(a)
print()
#[[0. 1. 0. 0. 0.]
# [0. 0. 1. 0. 0.]
# [0. 0. 0. 1. 0.]]

a = np.eye(3,5,k=-1)
print(a)
print()
#[[0. 0. 0. 0. 0.]
# [1. 0. 0. 0. 0.]
# [0. 1. 0. 0. 0.]]

#but you can't change the diagonal in identity
a = np.identity(4)
print(a)
print()


# multi-dimensional arrays with random integers
np.random.seed(0)

# Samples are uniformly distributed over the half-open interval [low, high)
a = np.random.uniform(low=0.5, high=10.0, size=(2, 3))
print(a)
print()
#[[5.71372829 7.29429898 6.22625207]
# [5.67639024 4.52472059 6.63599407]


# Create an array of the given shape and populate 
# it with random samples from a uniform distribution over [0, 1).
a = np.random.rand(2, 3)
print(a)
print()
#[[0.43758721 0.891773   0.96366276]
# [0.38344152 0.79172504 0.52889492]]



# Return random floats in the half-open interval [0.0, 1.0).
a = np.random.random((2, 3))
print(a)
print()
#[[0.56804456 0.92559664 0.07103606]
# [0.0871293  0.0202184  0.83261985]]


# Return random integers from the “discrete uniform” distribution 
# of the specified dtype in the “half-open” interval [low, high). 
# If high is None (the default), then results are from [0, low).
a = np.random.randint(0, 5, size=(2, 3))
print(a)
print()
#[[0 2 3]
# [0 1 3]]

# Return random integers from the “discrete uniform” distribution 
# of the specified dtype in the “half-open” interval [low, high). 
# If high is None (the default), then results are from [0, low).
a = np.random.randint(5, size=(2, 3))
print(a)
print()
#[[3 3 0]
# [1 1 1]]


# As of version 1.17, NumPy has a new random API.
# The recommended method for generating samples 
# from the uniform distribution on [0, 1) is:
rng = np.random.default_rng()  # Create a default Generator.
a = rng.random(size=(2,3))  
print(a)
print()



print('basic array operations')
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
# addition
print('addition: ', data + ones) # array([2, 3])
# subtraction
print('subtraction: ', data - ones) # array([0, 1])
# multiplication
print('multiplication: ', data * data) # array([1, 4])
# division
print('division: ', data / data) # array([1., 1.])
print()

# sum() - find  sum of all elements in an array
# works for 1D arrays, 2D arrays, and arrays in higher dimensions.
a = np.array([1, 2, 3, 4])
#np.sum(a)
print('sum: ', a.sum()) # 10
print()


# specify axis to add the rows or the columns in a 2D array
b = np.array([[1, 1], [2, 2]])
print(b)
print()

# sum the columns
c = b.sum(axis=0) # array([3, 3])
print(c)
print()

# sum the rows
c = b.sum(axis=1) # array([2, 4])
print(c)
print()


# in NumPy arrays, axis are zero-indexed and identify dimension
# in 2-d array has vertical axis (axis 0) and horizontal axis (axis 1)

A = np.array([[5, 3, 7, 1],
              [2, 6, 7 ,9],
              [1, 1, 1, 1],
              [4, 3, 2, 0]])

print(A.shape) # 4 x 4
print()

# max function - returns the largest value 
# in the entire array
print('max function')
print(A.max()) # 9
print()


# axis=0 - returns max in each column
# notice the returned array is flattened/aggregated
print('max along axis=0 (vertical)')
print(A.max(axis=0)) # array([5, 6, 7, 9])
print()

# axis=1 - returns max in each row
print('max along axis=1 (horizontal)')
print(A.max(axis=1)) # array([7, 9, 1, 4])
print()


# concatenation along different axis
A1 = np.array([[1,1,1],
               [1,1,1]])

A2 = np.array([[9,9,9],
               [9,9,9]])

print(A1)
print(A2)
print()

# concatenate along axis = 0
A_concat = np.concatenate([A1, A2], axis=0)
print('concatenate along axis = 0')
print(A_concat)
print()

# concatenate along axis = 1
A_concat = np.concatenate([A1, A2], axis=1)
print('concatenate along axis = 1')
print(A_concat)
print()


A1 = np.array([1,1,1])
A2 = np.array([9,9,9])
print(A1.shape)
print(A2.shape)
print()

# 3-D data
A1 = np.array([[[42, 34, 50, 66, 26],
             [27, 22, 32, 42, 17],
             [22, 18, 26, 34, 14]]])
print(A1.shape)

A2 = np.array([[[42, 34, 50, 66, 26],
             [27, 22, 32, 42, 17],
             [22, 18, 26, 34, 14]]])
print(A2.shape)

A_concat = np.concatenate([A1, A2], axis=1)
print(A_concat)
print(A_concat.shape)
print()

A_concat = np.concatenate([A1, A2], axis=2)
print(A_concat)
print(A_concat.shape)
print()


# Broadcasting
# carry out an operation between an array and a single number 
# (also called an operation between a vector and a scalar)
# or between arrays of two different sizes
print('Broadcasting')
data = np.array([1.0, 2.0])
a = data * 1.6
print(a)
print()

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
print(a * b) # array([ 2.,  4.,  6.])
print()

'''

a = np.array([1.0, 2.0, 3.0])
b = 2.0
print(a * b)
print()

print('Dot product')
a = np.array([1, 2])
b = np.array([3, 4])

dot = 0
for e, f in zip(a, b):
    dot += e * f
print(dot)

dot = 0
for i in range(len(a)):
    dot += a[i] * b[i]
print(dot)

a_prod_b = a*b # element-wise multiplication
print(a_prod_b)
dot = np.sum(a_prod_b)
print(dot)
dot = (a_prod_b).sum()
print(dot)
dot = np.dot(a,b)
print(dot)

print(A)
B = np.array([[1, 2, 3], [4, 5, 6]])
print(B)
print (A.dot(B))
print()

# matrix multiplication - inner dimensions should match
print(A.shape)
print(B.T.shape)
#print(A.dot(B.T))
print()
'''


'''
import numpy as np 

a = np.array([1, 2, 3])   # Create a rank 1 array
print(a)
print(a.shape)

# Create a vector as a row
vector_row = np.array([1, 2, 3])
print(vector_row.shape)

# Create a vector as a column
vector_column = np.array([[1],
                          [2],
                          [3]])
print(vector_column.shape)

u = np.array([2,1,3])
print(u)
uT = np.transpose(u)
print(uT)
print(np.dot(uT, u))
#v = np.transpose(np.array([[2,1,3]]))

'''

'''
# create array in numpy
A = np.array([1, 2, 3])
print('A: ', A)
print()

B = A + np.array([4])
print('A: ', A)
print('B: ', B)
print()
# Broadcasting is a powerful mechanism that allows 
# numpy to work with arrays of different shapes 

# regular vector addition
C = A + np.array([4, 4, 4])
print('C: ', C)
print()


# dot product
a = np.array([1, 2])
b = np.array([3, 4])

print(a.dot(b))

'''