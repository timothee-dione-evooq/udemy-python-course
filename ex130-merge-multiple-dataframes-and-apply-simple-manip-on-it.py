import pandas as pd

# Créer le DataFrame pour les livres
df_livres = pd.DataFrame({
    'BookID': ['B01', 'B02', 'B03', 'B04'],
    'Genre': ['Fiction', 'Science', 'Fiction', 'History']
})

# Créer le DataFrame pour les stocks
df_stocks = pd.DataFrame({
    'BookID': ['B01', 'B02', 'B03', 'B04'],
    'Stock': [20, 10, 30, 25]
})

merged_df = pd.merge(df_livres, df_stocks, how='inner', left_on='BookID', right_on='BookID')
result = merged_df.groupby('Genre').agg({'Stock': 'sum'}).rename(columns={'Genre': 'Genre', 'Stock': 'TotalStock'}).reset_index()

print(result)
