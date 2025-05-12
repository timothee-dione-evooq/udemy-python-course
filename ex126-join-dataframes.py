# Importer la bibliothèque Pandas.
import pandas as pd

# Créer les DataFrames.
data1 = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
         'Age': [25, 30, 22, 28],
         'Gender': ['F', 'M', 'M', 'F']}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
         'City': ['San Diego', 'Chicago', 'New York', 'San Diego']}
df2 = pd.DataFrame(data2)
result = pd.merge(df1, df2, how='inner', left_on='Name', right_on='Name')
#result = pd.concat(frames, axis=1, join='inner') -> results in dupplicated Name axis
print(result)