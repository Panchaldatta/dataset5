
# 2) Write a python programme to implement multiple linear regression model for stock 
# market data frame as follows: 
# Stock_Market = {'Year': 
# [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,20
# 16,2016,2016,2016,2016,2016,2016,2016,2016,2016], 
# 'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1], 
# 'Interest_Rate': 
# [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.7
# 5,1.75,1.75,1.75,1.75], 
# 'Unemployment_Rate': 
# [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6
# .2,6.1], 
# 'Stock_Index_Price': 
# [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,
# 958,971,949,884,866,876,822,704,719] } 
# And draw a graph of stock market price verses interest rate. 





import pandas as pd
import matplotlib.pyplot as plt
Stock_Market = {'Year': [2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016],
                'Month': [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                'Interest_Rate': [2.75, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.25, 2.25, 2.25, 2, 2, 2, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75],
                'Unemployment_Rate': [5.3, 5.3, 5.3, 5.3, 5.4, 5.6, 5.5, 5.5, 5.5, 5.6, 5.7, 5.9, 6, 5.9, 5.8, 6.1, 6.2, 6.1, 6.1, 6.1, 5.9, 6.2, 6.2, 6.1],
                'Stock_Index_Price': [1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075, 1047, 965, 943, 958, 971, 949, 884, 866, 876, 822, 704, 719]}
df = pd.DataFrame(Stock_Market, columns=[
    'Year', 'Month', 'Interest_Rate', 'Unemployment_Rate', 'Stock_Index_Price'])
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()



# import pandas as pd
# from sklearn import linear_model
# import statsmodels.api as sm
#
# data = {
#     'year': [2017, 2017, 2017, 2017, 2017,
#              2017, 2017, 2017, 2017, 2017,
#              2017, 2017, 2016, 2016, 2016,
#              2016, 2016, 2016, 2016, 2016,
#              2016, 2016, 2016, 2016],
#     'month': [12, 11, 10, 9,
#               8, 7, 6, 5, 4,
#               3, 2, 1, 12, 11,
#               10, 9, 8, 7, 6,
#               5, 4, 3, 2, 1],
#     'interest_rate': [2.75, 2.5, 2.5, 2.5, 2.5,
#                       2.5, 2.5, 2.25, 2.25, 2.25,
#                       2, 2, 2, 1.75, 1.75,
#                       1.75, 1.75, 1.75, 1.75, 1.75,
#                       1.75, 1.75, 1.75, 1.75],
#     'unemployment_rate': [5.3, 5.3, 5.3, 5.3, 5.4,
#                           5.6, 5.5, 5.5, 5.5, 5.6,
#                           5.7, 5.9, 6, 5.9, 5.8,
#                           6.1, 6.2, 6.1, 6.1,6.1,
#                           5.9, 6.2, 6.2, 6.1],
#     'index_price': [1464, 1394, 1357, 1293, 1256,
#                     1254, 1234, 1195, 1159, 1167,
#                     1130, 1075, 1047, 965, 943,
#                     958, 971, 949, 884, 866,
#                     876, 822, 704, 719]
#     }
#
# df = pd.DataFrame(data)
#
# x = df[['interest_rate', 'unemployment_rate']]
# y = df['index_price']
#
# # with sklearn
# regr = linear_model.LinearRegression()
# regr.fit(x, y)
#
# print('Intercept: \n', regr.intercept_)
# print('Coefficients: \n', regr.coef_)
#
# # with statsmodels
# x = sm.add_constant(x)  # adding a constant
#
# model = sm.OLS(y, x).fit()
# predictions = model.predict(x)
#
# print_model = model.summary()
# print(print_model)



# DM Assignment 5 set B-2
# #Write a python programme to implement multiple linear regression mod
# el for stock market data frame as follows:
import pandas as pd
import matplotlib.pyplot as plt
Stock_Market = {'Year':[2017,2017,2017,2017,2017,2017,2017,2017,20
17,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
'Interest_Rate':[2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.
75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
'Unemployment_Rate':[5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,
5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
'Stock_Index_Price':[1464,1394,1357,1293,1256,1254,1234,1195,1159,1
167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]}
df = pd.DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate'
,'Unemployment_Rate','Stock_Index_Price'])
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()