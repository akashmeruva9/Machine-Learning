import numpy as np

new_data = np.array([[2, 4, 6],
                     [8, 10, 12],
                     [14, 16, 18]])

new_file_path = 'new_output.txt'

np.savetxt(new_file_path, new_data, fmt='%d', delimiter=',')

print(f"New NumPy array saved to {new_file_path}")