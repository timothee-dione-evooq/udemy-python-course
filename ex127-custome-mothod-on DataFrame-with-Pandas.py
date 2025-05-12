# Importer la bibliothèque Pandas.
import pandas as pd

# Créer un DataFrame.
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva'],
        'Age': [25, 30, 22, 28, 35]}
df = pd.DataFrame(data)

# Définir la fonction pour mettre en majuscules les noms de plus de 4 caractères.
def capitalize_if_long(name):
    if len(name) > 4:
        return name.upper()
    else:
        return name

# Appliquer la fonction à la colonne 'Name'.
df['Name'] = df['Name'].apply(capitalize_if_long)

# Afficher le DataFrame modifié.
print(df)
