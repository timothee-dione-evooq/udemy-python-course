# Importer la bibliothèque Pandas.
import pandas as pd

# Créer un DataFrame.
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva'],
        'Age': [25, 30, 22, 28, 35],
        'Gender': ['F', 'M', 'M', 'F', 'F']}
df = pd.DataFrame(data)
print(df.rename(columns={'Name':'Nom','Age':'Âge','Gender':'Gender'}, inplace=True))