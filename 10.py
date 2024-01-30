import pandas as pd

new_data = {'Text': ['python', 'java', 'javascript', 'csharp', 'ruby']}
new_series = pd.Series(new_data['Text'])

new_word_lengths = new_series.str.len()

print("New Original Series:")
print(new_series)

print("\nNumber of characters in each word:")
print(new_word_lengths)
