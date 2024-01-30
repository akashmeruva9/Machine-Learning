import pandas as pd

new_data = {'Name': ['deepak', 'cherry', 'akash', 'srikari'],
            'Attempts': [2, 3, 1, 4],
            'Qualify': ['yes', 'no', 'yes', 'no']}

new_df = pd.DataFrame(new_data)

print("New DataFrame:")
print(new_df)

new_df['Qualify'] = new_df['Qualify'].replace({'yes': True, 'no': False})

print("\nNew DataFrame after replacing 'yes' and 'no' with True and False:")
print(new_df)