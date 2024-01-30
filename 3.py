import numpy as np

new_array1 = np.array([2, 4, 6, 8, 10])
new_array2 = np.array([4, 8, 12, 16])

new_result = np.isin(new_array1, new_array2)

print("New Array 1:", new_array1)
print("New Array 2:", new_array2)
print("Element-wise presence check:", new_result)