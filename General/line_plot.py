import matplotlib.pyplot as plt
import pandas as pd

stock = pd.read_csv('sample_stock_prices.csv', header=None, delimiter=',')

# assign names for each of the attributes, date and price
stock.columns = ['date','price']


# pd.to_datetime() function converts the date from the 
# character format to the date time format. 
# format: %d-%m-%Y argument specifies the format of the date in the input file.
stock['date'] = pd.to_datetime(stock['date'], format='%d-%m-%Y')

# stock.set_index() sets the date column as the index, 
# so that the price column can represent the time series data, 
# which is understood by the plot command.
indexed_stock = stock.set_index('date') 

ts = indexed_stock['price']

plt.plot(ts)

plt.show()
