# Importer la bibliothèque Pandas.
import pandas as pd

# Créer un DataFrame.
data = {'Product': ['A', 'B', 'A', 'C', 'B', 'C'],
        'Quantity': [5, 3, 4, 2, 1, 3],
        'Price': [20, 30, 20, 15, 30, 15]}
df = pd.DataFrame(data)

# Grouper par "Product" et effectuer des agrégations sur les colonnes "Quantity" et "Price".
result = df.groupby('Product').agg({'Quantity': 'sum', 'Price': 'mean'})

# Afficher le DataFrame groupé.
print(result)