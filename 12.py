import pandas as pd

data = {'Name': ['deepak', 'cherry', 'akash', 'srikari'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']}

index_labels = ['Person1', 'Person2', 'Person3', 'Person4']

df = pd.DataFrame(data, index=index_labels)

print(df)