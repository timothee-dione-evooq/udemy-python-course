import numpy as np

# Créer la classe MyArray.
class MyArray:
    def __init__(self, arr):
        self.arr = arr

    def shape(self):
        shape = np.shape(self.arr)
        print(f"{shape}")

my_arr = MyArray(np.array([[1, 2, 3], [4, 5, 6]]))
my_arr.shape()