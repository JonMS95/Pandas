import pandas as pd

PATH_WINE_REVS = '/home/jon/Desktop/scripts/ML/Pandas/Data_sets/winemag-data_first150k.csv'

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