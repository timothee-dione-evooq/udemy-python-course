from collections import Counter

marques = ['Nike', 'Adidas', 'Adidas', 'Adidas', 'Reebok', 'Reebok', 'New Balance', 'Nike', 'Puma', 'Nike', 'New Balance']

compteur = Counter(marques)
print(dict(compteur))