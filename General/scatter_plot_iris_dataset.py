import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris_dataset.csv', delimiter=',')
#print(iris)

# map each class of species (defined with descriptive names)
# to numeric codes as 0, 1, or 2
iris['species'] = iris['species'].map({"setosa" : 0, 
                                       "versicolor" : 1,
                                       "virginica" : 2})
#print(iris.species)

# c=iris.species specifies color mapping to different classes
# argument classes should be numeric
plt.scatter(iris.petal_length, iris.petal_width, c=iris.species)

plt.xlabel('petal length')
plt.ylabel('petal width')

plt.show()
