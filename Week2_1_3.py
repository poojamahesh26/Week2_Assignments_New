# ⁠Extract all numbers from A which are within a specific range. eg between 5 and 10.

import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# Define two custom numpy arrays A and B using values from iris_2d
A = iris_2d[:2]  # First two rows of the dataset
B = iris_2d[2:4]  # Next two rows of the dataset

print(A)
print(B)

filtered_A = A[(A >= 5) & (A <= 10)]
print("\nFiltered A (Numbers between 5 and 10):", filtered_A)
