# Importer la bibliothèque Pandas.
import pandas as pd

# Créer un DataFrame.
data = {'Year': [2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021],
        'Quarter': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)
df_pivot = df.pivot(index='Quarter', columns='Year', values='Sales')
print(df_pivot)
