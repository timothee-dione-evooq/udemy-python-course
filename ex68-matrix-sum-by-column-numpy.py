# Importer la bibliothèque NumPy.
import numpy as np

# Créer une matrice NumPy.
matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
columns_sum =np.sum(matrice, 0)
print(columns_sum)