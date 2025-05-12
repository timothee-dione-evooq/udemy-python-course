# Importer la bibliothèque Pandas.
import pandas as pd

# Créer les DataFrames.
products = pd.DataFrame({'ProductID': ['P01', 'P02', 'P03', 'P04', 'P05'],
                         'Category': ['Electronics', 'Electronics', 'Clothing', 'Electronics', 'Clothing']})

prices = pd.DataFrame({'ProductID': ['P01', 'P02', 'P03', 'P04', 'P05'],
                       'Price': [100, 150, 200, 250, 300]})

sales = pd.DataFrame({'ProductID': ['P01', 'P02', 'P03', 'P04', 'P05'],
                      'Sales': [10, 20, 30, 40, 50]})

merged_df = pd.merge(products, prices, on='ProductID', how='inner')
merged_df = pd.merge(merged_df, sales, on='ProductID', how='inner')

# Calculer la recette totale pour chaque produit
merged_df['Revenue'] = merged_df['Price'] * merged_df['Sales']

grouped_df = merged_df.groupby('Category').agg(
    MeanRevenue=('Revenue', 'mean'),
    TotalRevenue=('Revenue', 'sum')
)

global_revenue = merged_df['Revenue'].sum()

grouped_df['Percentage'] = grouped_df['TotalRevenue'] / global_revenue * 100

print(grouped_df)