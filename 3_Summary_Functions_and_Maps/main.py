import pandas as pd
import numpy as np

#Numpy is imported just to insert Nan values (NaN stands for Not a Number).

PATH_WINE_REVS = '/home/jon/Desktop/scripts/ML/Pandas/Data_sets/winemag-data-130k-v2.csv'

reviews = pd.read_csv(PATH_WINE_REVS, index_col = 0)

# Data from a DataFrame may be summarized. This way, mean values, percentiles and so on may be described in a friendly way.
reviews_summary = reviews.describe()
print(reviews_summary)

# Series may be also summarized:
reviews_points_summary = reviews.points.describe()
print(reviews_points_summary)

# The examples seen above only cover numeric values. String type values can be also summarized. The data is also slightly different: unique values,
# frequencies or counts are displayed in this case.
reviews_taster_names = reviews.taster_name.describe()
print(reviews_taster_names)

# Particular values from a summary may be accessed by using their names. Just access them as it's done for a common class attribute.
reviews_points_mean = reviews.points.mean()
print(reviews_points_mean)

# It may happen that some values get repeated along a column. If the aim is to know the names, and not how many times the appear within a column, the
# unique() method should be used.
print(reviews.taster_name.unique())

# Maps are another data type that can be obtained from a DataFrame. Similar to dictionaries, maps are a way to associate some data set values to other.
# Let's see it first with a simple example:
simple_example = pd.Series(["Rabbit", 'Dog', np.nan, 'Cat'])

# If the names of the animals are wanted to be substituted by their hatchlings' names, a dictionary should be used. For each key found in the dict,
# the target value will be replaced by the value shown as dictionary value. If any member of the series is not found within the dictionary keys,
#it will be replaced by NaN.
simple_example_maped = simple_example.map({'Dog': 'Puppy', 'Cat': 'Kitten'})
print()
print(simple_example)
print()
print(simple_example_maped)

# It's worth it pointing out that map function also allows functions as input parameters. This way, a value may be replaced by other depending on which
# the output of that function is. In this case, each value of a Series object is going to be multiplied by two.
simple_example_2 = pd.Series([1, 4, 7, 10], name = 'numbers')
simple_example_2_maped = simple_example_2.map(lambda a : a * 2)
print()
print(simple_example_2)
print()
print(simple_example_2_maped)

# Let's say that the mean value is wanted to be moved to 0 (thus, values over the mean will be over zero, otherwise, they will be below zero). The proper
# way to do this is to subtract the mean value to each memeber in the Series. In this case, it will be done with the 'points' Series.
reviews_points_0_mean = reviews.points.map(lambda p : p - reviews_points_mean)
print()
print(reviews.points)
print()
print(reviews_points_0_mean)

# OK, this is for the Series. But what about the DataFrames? Well in this case, the analogous method is called 'apply', which affects each row.
def remean_points(row):
    row.points -= reviews_points_mean
    return row
reviews.apply(remean_points, axis = 'columns')