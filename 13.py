import pandas as pd

new_data = {'Name': ['Cherry', 'Deepak', 'Meruva', 'Akash', 'Srikari'],
            'Attempts': [4, 5, 2, 3, 4],
            'Score': [89, 95, 70, 85, 92]}

new_df = pd.DataFrame(new_data)

new_result_df = new_df[new_df['Attempts'] > 2]

print("New DataFrame:")
print(new_df)

print("\nSelected rows where the number of attempts is greater than 2:")
print(new_result_df)