import pandas as pd

new_data = {'Name': ['deepak', 'cherry', 'akash', 'srikari'],
            'Attempts': [2, 3, 1, 4],
            'Score': [85, 78, 92, 89]}

new_df = pd.DataFrame(new_data)

print("New DataFrame:")
print(new_df)

new_df = new_df.sort_values(by=['Name', 'Score'], ascending=[False, True])

print("\nSorted DataFrame:")
print(new_df)