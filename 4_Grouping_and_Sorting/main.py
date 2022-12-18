import pandas as pd

PATH_WINE_REVS = '/home/jon/Desktop/scripts/ML/Pandas/Data_sets/winemag-data-130k-v2.csv'

# Maps allow the user to transform the data within a DataFrame or Series in a specified way. However, sometimes
# user may want to group the data by following some criteria. This is achieved by using the groupby() function.
reviews = pd.read_csv(PATH_WINE_REVS, index_col = 0)
print(reviews.columns)

# In this case, we are gonna start by separating the data in groups depending on their points. 
print(reviews.groupby('points').points.count())
# Basically, what we have done is just to separate them by their points, then counting how many rows have the same
# value given the grouping criterion.

# Luckily, a shortcut exists to the line shown above: value_counts()
print(reviews['points'].value_counts())

# If we want to know which is the cheapest wine for each point score:
print(reviews.groupby('points').price.min())

# Same as shown in the previous exercise, apply() function (which was used for mapping DataFrames) can be used here
# as well. For example, if the first element of each group is wanted to be modified:
reviews.groupby('winery').apply(lambda df : df.title.iloc[0])