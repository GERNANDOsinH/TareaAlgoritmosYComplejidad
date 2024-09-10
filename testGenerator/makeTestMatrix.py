import numpy as np

matrix = []

for i in range (2, 6):
    matrix.append(np.random.rand(2**i, 2**i))
    matrix.append(np.random.rand(2**i, 2**i))

with open('testMatrix.bin', 'wb') as file:
    for M in matrix:
        np.save(file, M)