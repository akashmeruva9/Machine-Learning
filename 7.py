import pandas as pd

new_data = {'X': 15, 'Y': 25, 'Z': 35, 'W': 45, 'K': 55}
new_series = pd.Series(new_data)

new_condition = new_series <= 25

new_subset_series = new_series[new_condition]

print("New Original Series:")
print(new_series)

print("\nNew Subset Series based on new condition:")
print(new_subset_series)