import pandas as pd

PATH_WINE_REVS = '/home/jon/Desktop/scripts/ML/Pandas/Data_sets/winemag-data_first150k.csv'

# Let's start by instantiating a DataFrame from the wine reviews CSV file, using the first column of it as index:
reviews = pd.read_csv(PATH_WINE_REVS, index_col = 0)
print(reviews.head(n = 10))

# If displaying a Series (it's to say, a column from the DataFrame), first it may be wanted the column names of the DataFrame. To do so, use the 'columns'
# class attribute.
print(reviews.columns)

# Now that the Series names are known, choose which to print by using either DataFrame.ColName or DataFrame['ColName'] syntaxes. Second one is a more general
# option, as the name can be always typed correctly, even if it contains spaces or any ther special character within it. Note that not all the Series have to
# be printed: head method is also available for singles, not only for the whole DataFrame.
print(reviews['country'].head())

# As seen in the previous exercise, DataFrames are instantiated by using a dictionary which usually contains a key (that's associated to the Series' name), as
# well as a list, which contains the values for each Series data entry. These values may be accessed same as it's done with a Python list object. For example,
# if the first value in the 'country' Series is wanted to be known:
print(reviews['country'][0])

# However, Pandas has its own access oprators, which are the ones that are supossed to be used: loc and iloc. Both of them take [row, column] as input parameter.
# With iloc, which is index based, a range can be passed for both input parameter members:
print(reviews.iloc[1:3, 0])

# It's also possible to pass just some numbers as parameters:
print(reviews.iloc[[1, 4, 7], 0])

# On the other hand, loc may be used also when labels instead of numbers are used for indexing. For example, let's say that the target is to get the third
# element of the 'country' Series:
print(reviews.loc[3, 'country'])

# More than a single column or row may be used:
print(reviews.loc[[3, 4], [reviews.columns[0], reviews.columns[1], reviews.columns[2]]])

# Despite having created the DataFrame by using a particular column index, it can be manipulated after. For that purpose, set_index class method can be used:
reviews.set_index("country") 
print(reviews.head())

# Conditional selection can be performed in DataFrames. If, for example, if a review is from Italian wine or not is wanted to be shown:
print(reviews['country'] == 'Italy')

# Following this path, loc method can be used to access only the rows which country is Italy:
print(reviews.loc[reviews['country'] == 'Italy'])

# Combined logic is allowed here:
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])