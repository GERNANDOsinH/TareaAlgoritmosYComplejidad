import numpy as np


# Caso Identidad, una de las matrices es la identidad y los elementos estan generados de manera aleatoria.
matrix0 = np.eye(64)
matrix1 = np.random.randint(-100, 101, size=(64, 64))

# Caso al Cuadrado, se eleva al cuadrado una unica matriz(multiplicar por si misma).
matrix2 = np.random.randint(-100, 101, size=(64, 64))
    
# Caso aleatorio, los elementos de ambas matrices estan generados de manera "aleatoria".
matrix3 = np.random.randint(-100, 101, size=(64, 64))
matrix4 = np.random.randint(-100, 101, size=(64, 64))

np.savez('testMatrix.npz',
         matriz1_0=matrix0, matriz2_0=matrix1,
         matriz1_1=matrix2, matriz2_1=matrix2,
         matriz1_2=matrix3, matriz2_2=matrix4
         )