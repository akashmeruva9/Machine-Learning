import pandas as pd

new_data = {'Name': ['deepak', 'cherry', 'akash', 'meruva', 'srikari'],
            'Attempts': [2, 3, 1, 4, 5],
            'Score': [85, 78, 92, 89, 94]}

new_df = pd.DataFrame(new_data)

print("New DataFrame:")
print(new_df)

new_row = {'Name': 'NewPerson', 'Attempts': 5, 'Score': 85}
new_df = new_df.append(new_row, ignore_index=True)

print("\nNew DataFrame with the new row:")
print(new_df)

new_df = new_df.drop(index=new_df.index[-1])

print("\nNew DataFrame after deleting the new row:")
print(new_df)