import pandas as pd

new_data = {'Numbers': [8, 12, 18, 22, 25, 32, 40, 45]}
new_series = pd.Series(new_data['Numbers'])

new_positions_of_multiples_of_5 = new_series.index[new_series % 5 == 0]

print("New Original Series:")
print(new_series)

print("\nNew Positions of numbers that are multiples of 5:")
print(new_positions_of_multiples_of_5)
