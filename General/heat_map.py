import matplotlib.pyplot as plt
import pandas as pd

wine_quality = pd.read_csv('winequality.csv', delimiter=';')

# The wine_quality.corr() method returns a correlation 
# matrix for all the attributes in the dataset.

# pandas.DataFrame.corr
# DataFrame.corr(method='pearson', min_periods=1)[source]
# Compute pairwise correlation of columns, excluding NA/null values.
corr = wine_quality.corr()

# The correlation values range from -1 (highly negative) 
# to +1 (highly positive). 
# Negative values are represented from red to black, 
# and positive values are represented from dark yellow to white. 
# Pure white is +1, which is the highest positive correlation, 
# and pure black is the highest negative correlation.

plt.figure(figsize=(12,9))

plt.imshow(corr,cmap='hot')

plt.colorbar()

plt.xticks(range(len(corr)),corr.columns, rotation=20)
plt.yticks(range(len(corr)),corr.columns)

plt.show()


The correlation values range from -1 (highly negative) to +1 (highly positive). Negative values are represented from red to black, and positive values are represented from dark yellow to white. Pure white is +1, which is the highest positive correlation, and pure black is the highest negative correlation.
As expected, all diagonal boxes are white, as they are a correlation with themselves, which has to be +1. The correlation between the pH and fixed acidity values is black, which means highly negative, close to -1


