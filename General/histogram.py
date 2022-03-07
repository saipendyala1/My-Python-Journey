
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

grp_exp = np.array([12, 15, 13, 20, 19, 20, 11, 19, 11, 12, 19, 13, 12, 
                    10, 6, 19, 3, 1, 1, 0, 4, 4, 6, 5, 3, 7, 12, 7, 9, 
                    8, 12, 11, 11, 18, 19, 18, 19, 3, 6, 5, 6, 9, 11, 
                    10, 14, 14, 16, 17, 17, 19, 0, 2, 0, 3, 1, 4, 6, 
                    6, 8, 7, 7, 6, 7, 11, 11, 10, 11, 10, 13, 13, 15, 
                    18, 20, 19, 1, 10, 8, 16, 19, 19, 17, 16, 11, 1, 
                    10, 13, 15, 3, 8, 6, 9, 10, 15, 19, 2, 4, 5, 6, 9, 
                    11, 10, 9, 10, 9, 15, 16, 18, 13])


# data is divided into 21 bins of equal size, 
# by specifying nbins = 21
nbins = 21 

# plt.hist() plots the histogram with grp_exp and nbins as arguments.
# returns three parameters, 
# n, bins, and patches. 
# n is the list containing the number of items in each bin
# bins is another list specifying starting point of the bin,
# patches is the list of objects for each bin. 

n, bins, patches = plt.hist(grp_exp, bins = nbins)

plt.xlabel("Experience in years")
plt.ylabel("Frequency")
plt.title("Distribution of Experience in a Lateral Training Program")

plt.axvline(x=grp_exp.mean(), linewidth=2, color = 'r') 

plt.show()


