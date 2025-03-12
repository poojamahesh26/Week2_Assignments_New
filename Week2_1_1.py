import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# Define two custom numpy arrays A and B using values from iris_2d
A = iris_2d[:2]  # First two rows of the dataset
B = iris_2d[2:4]  # Next two rows of the dataset

print(A)
print(B)

# Generate two new numpy arrays by stacking A and B vertically and horizontally
vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

print("Vertical Stack:\n", vertical_stack)
print("\nHorizontal Stack:\n", horizontal_stack)