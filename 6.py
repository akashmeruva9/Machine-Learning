import pandas as pd

new_series_of_lists = pd.Series([[10, 20, 30, 40], [50, 60], [70, 80, 90]])

new_result_series = new_series_of_lists.explode()

print("New Original Series:")
print(new_series_of_lists)

print("\nNew Converted Series:")
print(new_result_series)
