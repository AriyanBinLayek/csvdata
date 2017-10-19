import pandas as pd
import numpy as np

# Insert to a dataframe
df = pd.DataFrame()

# read a csv file in dataframe
new = df.from_csv('lastFSG.csv', index_col='Name')


# function for grouping data
def cluster(x, upper_li, lower_li):
    mid = (upper_li + lower_li) / 2
    mid = mid
    if x < lower_li:
        msg = 'Less then ' + str(lower_li)
    elif x >= lower_li and x < mid:
        msg = str(lower_li) + ' - ' + str(mid)
    elif x >= mid and x < upper_li+1:
        msg = str(mid) + ' - ' + str(upper_li)
    else:
        msg = 'Greter then ' + str(upper_li)
    return msg


# input upper limit and lower limit
upper_li = input('Input upper limit: ')
lower_li = input('Input lower limit: ')

# create a new column after grouping a column data
new['SKCondition'] = new.iloc[:, 10].apply(cluster, args=(upper_li, lower_li))

# show csv file data
print(new)

# write a new csv file
new.to_csv('lastSK.csv')
