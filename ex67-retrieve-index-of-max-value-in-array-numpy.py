# Importer la bibliothèque NumPy.
import numpy as np

# Créer un tableau NumPy.
tableau = np.array([3, 7, 2, 1, 9, 5])
maximum = np.max(tableau,0)
index = tableau.tolist().index(maximum)
print(index)