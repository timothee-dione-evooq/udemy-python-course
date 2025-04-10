# Importer la bibliothèque NumPy.
import numpy as np

# Créer un tableau NumPy.
tableau = np.array([1, 5, 9, 3, 6, 7, 2, 4, 8])
tableau_sans_valeurs_superieures_a_5 = np.where(tableau <= 5, tableau, 0)
print(tableau_sans_valeurs_superieures_a_5)