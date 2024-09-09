import numpy as np

with open('testMatrix.bin', 'wb') as testMatrix:
    # Caso Identidad, una de las matrices es la identidad y los elementos estan generados de manera aleatoria.
    matrix0 = np.eye(100)
    matrix1 = np.random.randint(-100, 101, size=(100, 100))
    matrix0.tofile(testMatrix)
    matrix1.tofile(testMatrix)

    # Caso al Cuadrado, se eleva al cuadrado una unica matriz(multiplicar por si misma).
    matrix0 = np.random.randint(-100, 101, size=(100, 100))
    matrix0.tofile(testMatrix)
    matrix0.tofile(testMatrix)
    
    # Caso aleatorio, los elementos de ambas matrices estan generados de manera "aleatoria".
    matrix0 = np.random.randint(-100, 101, size=(100, 100))
    matrix1 = np.random.randint(-100, 101, size=(100, 100))
    matrix0.tofile(testMatrix)
    matrix1.tofile(testMatrix)