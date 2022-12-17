# First step: import pandas library.
import pandas as pd

# Add some definitions.
PATH_WINE_REVS  = '/home/jon/Desktop/scripts/ML/Pandas/Data_sets/winemag-data_first150k.csv'

# A DataFrame is a table. It contains data entries in each values, same as an Excel sheet. There are also Series, which are just columns of a DataFrame.
first_DataFrame = pd.DataFrame({'Yes':[50, 21], 'No': [131, 2]})
print(first_DataFrame)
# As seen in the printed lines, keys of the dictionary used as input parameter for the DataFrame constructor method are then represented as the names of the
# columns, while values (associated to each keys) are the values of each Series (each Series is made of the name of the column, i.e., keys, and the values are
# the integers stored n each list in this case).

# The Dataframe values may not be limited to integers:
second_DataFrame = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue':['Pretty good.', 'Bland.']})
print(second_DataFrame)

# Apart from using a dictionary, a list containing each row's name may be used to provide the DataFrame with enough data to do so. Note that the number of elements
# within the list of row names within the 'index' input parameters, and the number of values associated to each dictionary keys passed in the first parameter
# should always be the same.
third_DataFrame = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue':['Pretty good.', 'Bland.']}, index = ['Product A', 'Product B'])
print(third_DataFrame)

# As stated before, a series is just a list of data, that may conform a column of a DataFrame object.
first_Series = pd.Series([1, 2, 3, 4, 5])
print(first_Series)

# Same as in a Dataframe, names can be associated to each row in a Series. However, the column of a Series os not going to have a name. Anyway, a name can be
# given to the whole series, by passing the input parameter 'name'.
second_Series = pd.Series([30, 35, 40], index = ['2015 Sales', '2016 Sales', '2017 Sales'], name = 'Product A')
print(second_Series)

# Most of the times, DataFrames are not created by hand, but they are imported from a CSV file. It's not recommended to print it as a data frame, as it contains
# hundreds of thousands of reviews. Anyway, its size may be known by referencing reviews_shape class attribute:
wine_reviews = pd.read_csv(PATH_WINE_REVS)
print(wine_reviews.shape)

# On the other hand, reading a few rows from the DataFrame is worth it generally. It can be done by using the 'head' method. The input parameter of this method
# is the number of rows that are meant to be displayed, which is 5 by default, although it can be modified.
print(wine_reviews.head())

# As seen when printed, an index by default is associated to each row. Luckily, an arbitrary column may be used as index as well. Just specify it by providing
# a value to the 'index_col' input parameter:
wine_reviews = pd.read_csv(PATH_WINE_REVS, index_col = 0)
print(wine_reviews.head())