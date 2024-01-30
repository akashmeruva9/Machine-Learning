import pandas as pd
import numpy as np

new_data = {'A': [3, 6, np.inf, 9],
            'B': [np.inf, 11, 13, 15]}

new_df = pd.DataFrame(new_data)

print("New DataFrame:")
print(new_df)

new_df.replace([np.inf, -np.inf], np.nan, inplace=True)

new_df = new_df.dropna()

print("\nNew DataFrame after removing infinite values:")
print(new_df)