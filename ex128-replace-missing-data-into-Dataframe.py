# Importer la bibliothèque Pandas.
import pandas as pd
import numpy as np

# Créer un DataFrame.
data = {'CustomerID': ['C1', 'C2', 'C3', 'C4', 'C5'],
        'Age': [30, 35, 25, 28, 32],
        'Income': [50000, np.nan, 40000, 45000, np.nan]}
df = pd.DataFrame(data)

median_income = df['Income'].median()
print(median_income)

df['Income'].fillna(median_income, inplace=True)
print(df)