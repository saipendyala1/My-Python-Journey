# pandas is a fast, powerful, flexible and easy 
# to use open source data analysis and manipulation tool,
# built on top of the Python programming language.

import pandas

# read csv file in pandas
df = pandas.read_csv('employee_data.csv')

#Pandas reads the dataset and stores it 
#as a DataFrame object 
print(type(df))
print()

# check amount of data
print(len(df))
# .shape provides the dimensionality of data
print(df.shape)
print()


# look at the first five rows
print(df.head())
print()

# 1. pandas recognized that the first line of the CSV
#    contained column names, and used them automatically. 
# 2. pandas is also using zero-based integer indices in the DataFrame. 
#    we can specify what our index should be.
# 3. pandas has properly converted the Salary and 
#    Sick Days remaining columns to numbers, 
#    but the Hire Date column is still a String

print('Hire Date column: ', type(df['Hire Date'][0]))
print()


# use a different column as the DataFrame index, 
# add the index_col optional parameter

df = pandas.read_csv('employee_data.csv', index_col='Name')
print(df)
print()

# force pandas to read data as a date with 
# the parse_dates optional parameter
df = pandas.read_csv('employee_data.csv',
                     index_col='Name', 
                     parse_dates=['Hire Date'])
print(df)
print()

print('Hire Date column: ', type(df['Hire Date'][0]))
print()


# Read the file
data = pandas.read_csv('sample_data.csv')
print(data)
print()

# loc is label-based, which means that we have to specify the 
# name of the rows and columns that we need to filter out.

# select all rows with a condition
data_age = data.loc[data.age >= 15]
print(data_age)
print()

'''

# select with multiple conditions
data_age_gender = data.loc[(data.age >= 12) & (data.gender == 'M')]
print(data_age_gender)
print()

#slice data - select specific rows
slice_data = data.loc[1:3]
print(slice_data)
print()

# select only required columns with a condition
col_cond_data = data.loc[(data.age >= 12), ['city', 'gender']]
print(col_cond_data)
print()

# iloc is integer index-based, we specify rows and columns 
# by their integer index.

slice_data = data.iloc[[0,2]]
print(slice_data)
print()


# Read the file
df = pandas.read_csv('scripts.csv')

# Assign first_dialogue to the first row's "Dialogue" column
first_dialogue = df.loc[0, "Dialogue"]
print(first_dialogue)

'''