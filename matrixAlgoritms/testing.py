import numpy as np
import cProfile

from mulMatrix import multiplicar_matrices
from mul2Matrix import multiplicarMatrices
from strassen import strassen

data = np.load('matrixAlgoritms/testMatrix.npz')
print("Claves en el archivo NPZ:", data.files)
pairMatrix = []

for i in range(len(data.files) // 2):
    matriz1 = data[f'matriz1_{i}']
    matriz2 = data[f'matriz2_{i}']
    pairMatrix.append((matriz1, matriz2))

for M0, M1 in pairMatrix:
    print(f"Profiling matrices of shape {M0.shape} and {M1.shape}")
    cProfile.run('multiplicar_matrices(M0, M1)')
    cProfile.run('multiplicarMatrices(M0, M1)')
    cProfile.run('strassen(M0, M1)')