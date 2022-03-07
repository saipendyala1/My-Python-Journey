import matplotlib.pyplot as plt
import pandas as pd

# plt.figure(figsize=(10,6)) overwrites the 
# default figure size with size (10, 6).
plt.figure(figsize=(10,6))

# pd.read_excel() reads the data and assigns 
# values to the x and yaxes coordinates.
age_weight = pd.read_excel('scatter_ex.xlsx', 'age_weight')

x = age_weight['age']
y = age_weight['weight']

# plt.scatter(x,y) plots the scatter plot.
plt.scatter(x, y)

# set x and y axes labels
plt.xlabel('Age')
plt.ylabel('Weight')

plt.show()