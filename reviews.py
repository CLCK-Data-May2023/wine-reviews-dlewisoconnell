import pandas as pd

wine_data = pd.read_csv('data/winemag-data-130k-v2.csv')

summary = wine_data.groupby('country').agg({'country': 'count', 'points': 'mean'}).rename(columns={'country': 'count', 'points': 'average_points'})

summary['average_points'] = summary['average_points'].round(1)

summary.reset_index(inplace=True)

summary.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data has been written to 'data/reviews-per-country.csv'.")
