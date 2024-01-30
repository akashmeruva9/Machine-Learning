import pandas as pd

new_data = {'Category': ['X', 'Y', 'X', 'Z', 'Y', 'X', 'X', 'Z', 'Z']}
new_series = pd.Series(new_data['Category'])

new_most_frequent_value = new_series.mode()[0]

new_modified_series = new_series.where(new_series == new_most_frequent_value, 'Other')

print("New Original Series:")
print(new_series)

print("\nNew Modified Series:")
print(new_modified_series)
