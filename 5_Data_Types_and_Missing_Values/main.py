import pandas as pd

# The data type for a column in a DataFrame or Series is known as the "dtype".

PATH_WINE_REVS = '/home/jon/Desktop/scripts/ML/Pandas/Data_sets/winemag-data-130k-v2.csv'
PATH_WINE_REVS_NOT_NULL_COUNTRY = '/home/jon/Desktop/scripts/ML/Pandas/Modified_data_sets/winemag-data-130k-v2-not-null-country.csv'
PATH_WINE_REVS_NOT_NULL_COUNTRY_KERINO = '/home/jon/Desktop/scripts/ML/Pandas/Modified_data_sets/winemag-data-130k-v2-not-null-country-kerino.csv'
LINE_SEPARATOR = "*" * 60
print(LINE_SEPARATOR)
print("Reviews overview:")
reviews = pd.read_csv(PATH_WINE_REVS, index_col=0)
# In the line above, the first ("0-th") column was chosen as the index column, just to prevent the generated csv
# files to repeat the index (it's to say, to add a second index column when reading or writing it).
print(reviews)
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

# As seen in previous chapters, if the aim is to print some columns within the DataFrame, an array of column
# names can be used. On top of that, columns that are null or not null can be selected as well, by using the
# pd.isnull or pd.isnotnull methods.
print(LINE_SEPARATOR)
print(reviews.columns)
# Let's say, for example, that what is wanted os to show all the rows of the DataFrame where the country field
# is marked as NaN (which, by the way, is a float64 kind of special value):
print(LINE_SEPARATOR)
print(reviews[pd.isnull(reviews.country)])
# Same can be done for all of those which contain a not null value:
print(LINE_SEPARATOR)
print(reviews[pd.notnull(reviews.country)])

# As it's featured in the second chapter of the Intermediate ML series, replacing null values is a common mistake
# correction operation. This can be achieved by using the "fillna" pandas built-in method:
print(LINE_SEPARATOR)
reviews.country = reviews.country.fillna("Unknown")
reviews.to_csv(PATH_WINE_REVS_NOT_NULL_COUNTRY)
print("Line 913, which had a NaN value in the country column before replacing it.")
print(reviews.iloc[913])

# There's no need for the cell to store a NaN value for it to be replaced. Let's say that the twitter account of
# a taster whose nickname is "@kerinokeefe" has been changed to "@kerino" (twitter account nicknames are stored
# within the taster_twitter_handle column). "replace(first_val, second_val)" method can be used in this case for
# the explained purpose:
print(LINE_SEPARATOR)
reviews.taster_twitter_handle = reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
print(reviews)
reviews.to_csv(PATH_WINE_REVS_NOT_NULL_COUNTRY_KERINO)