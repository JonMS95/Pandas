import pandas as pd

# The data type for a column in a DataFrame or Series is known as the "dtype".

PATH_WINE_REVS = '/home/jon/Desktop/scripts/ML/Pandas/Data_sets/winemag-data-130k-v2.csv'
LINE_SEPARATOR = "*" * 60

reviews = pd.read_csv(PATH_WINE_REVS)
print(LINE_SEPARATOR)
print("Type of data in the \"price\" column of the \"reviews\" DataFrame:", end='\t')
print(reviews.price.dtype)

# If what is wanted is to get the data type of every column in the dataset, then the "dtypes" property of the
# DataFrame can be addresses for this purpose. Note that the referenced property is dtypes instead of dtype in
# this case, as more than a single data type is meant to be known.
print(LINE_SEPARATOR)
print("Data type of every column in the \"reviews\" DataFrame:")
print(reviews.dtypes)

# As seen when executed the line above, columns that contain string type data are marked as 'object' type.
# On top of that, casting is enabled for the whole Series or DataFrame columns. Use the "astype(type)" method.
# As an example, points are by nature an int64 data type column, but they can be displayed as if they were flot64.
print(LINE_SEPARATOR)
print(reviews.points.astype('float64'))

# Index of a DataFrame or Series have their own data type too:
print(LINE_SEPARATOR)
print(reviews.index.dtype)

print(LINE_SEPARATOR)