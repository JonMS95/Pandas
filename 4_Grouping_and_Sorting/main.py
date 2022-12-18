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

# Another groupby ethod worth mentioning is agg(), which lets the developer apply several functions on the DataFrame
# simultaneously. For example, it can be used to have a simple statistical summary of the grouped DataFrame.
# Let's say we want to know how many prices are there for each country, as well as its min and max values.
statsByCountry = reviews.groupby('country').price.agg([len, min, max])
print(statsByCountry)

# Until this point, single indexes have been used. However, more than one index can be used to get some more
# accurate data. For example, data can be grouped by country, then by province:
countries_and_provinces = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_and_provinces)

# As seen, the index is now made of two labels: country and province. If the numerical index is wanted to by set
# again, reset_index() method should be used:
countries_and_provinces.reset_index()
print(countries_and_provinces)

# Values can be sorted too. Just use the sort_values() method, using the desired criterion as input parameter.
# Note that different from agg method, sort_values uses strings as input parameters for 'by' argument.
countries = reviews.groupby('country').description.agg([len])
countries.reset_index()
countries.sort_values(by = 'country')
print("*********")
print(countries)