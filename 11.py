import pandas as pd

new_data = {'YearMonth': ['2023-05', '2023-06', '2023-07', '2023-08']}
new_series = pd.Series(new_data['YearMonth'])

new_day_of_month = 10

new_result_dates = pd.to_datetime(new_series + '-' + str(new_day_of_month), format='%Y-%m-%d')

print("New Original Series:")
print(new_series)

print("\nNew Resulting Dates:")
print(new_result_dates)
