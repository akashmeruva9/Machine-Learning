import numpy as np

array_with_missing_data = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])

missing_indices = np.isnan(array_with_missing_data)

print("Original array:", array_with_missing_data)
print("Missing data indices:", missing_indices)
