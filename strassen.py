import numpy as np

def next_power_of_two(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def strassen(A, B):
    # Dimensiones de las matrices originales
    m, n = A.shape
    p, q = B.shape

    # Dimensiones ajustadas a la siguiente potencia de 2
    size = max(next_power_of_two(max(m, n)), next_power_of_two(max(p, q)))

    # Rellenar las matrices con ceros para que sean de tamaño "size x size"
    A_padded = np.zeros((size, size))
    B_padded = np.zeros((size, size))
    A_padded[:m, :n] = A
    B_padded[:p, :q] = B

    # Ejecutar Strassen en las matrices rellenadas
    C_padded = _strassen_recursive(A_padded, B_padded)

    # Recortar la matriz resultante al tamaño original
    return C_padded[:m, :q]

def _strassen_recursive(A, B):
    n = len(A)
    
    # Caso base: multiplicación directa para matrices 1x1
    if n == 1:
        return A * B
    
    # Dividir las matrices en submatrices de tamaño n/2 x n/2
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Calcular los productos intermedios
    M1 = _strassen_recursive(A11 + A22, B11 + B22)
    M2 = _strassen_recursive(A21 + A22, B11)
    M3 = _strassen_recursive(A11, B12 - B22)
    M4 = _strassen_recursive(A22, B21 - B11)
    M5 = _strassen_recursive(A11 + A12, B22)
    M6 = _strassen_recursive(A21 - A11, B11 + B12)
    M7 = _strassen_recursive(A12 - A22, B21 + B22)

    # Calcular las submatrices del resultado
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combinar submatrices en una matriz de resultado
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C