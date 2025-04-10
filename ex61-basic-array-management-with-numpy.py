# Importer la bibliothèque NumPy.
import numpy as np
arr = np.empty(0, dtype=int)
for x in range(10, 55, 5):
  arr = np.append(arr, x)
print(arr)