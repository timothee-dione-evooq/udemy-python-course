# Importer la bibliothèque NumPy.
import numpy as np

# Créer deux tableaux NumPy.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.matmul(A,B)
print(C)