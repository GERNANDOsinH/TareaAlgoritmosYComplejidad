import numpy as np

def split(source):
    # Descripción: Genera 4 sub-matrices de la matriz de entrada.
    mid = len(source) // 2

    A = source[:mid, :mid]
    B = source[:mid, mid:]
    C = source[mid:, :mid]
    D = source[mid:, mid:]

    return A, B, C, D

def strassen(X, Y):
    # Descripción: Algoritmo de multiplicación de matrices basado en la metodología dividir y vencer
    # que multiplica dos matrices cuadradas mediante dividir las matrices en sub-matrices y llamadas
    # recursivas.
    if X.shape[0] == 1:
        return X * Y
    
    A0, B0, C0, D0 = split(X)
    A1, B1, C1, D1 = split(Y)

    M1 = strassen(A0 + D0, A1 + D1)
    M2 = strassen(C0 + D0, A1)
    M3 = strassen(A0, B1 - D1)
    M4 = strassen(D0, C1 - A1)
    M5 = strassen(A0 + B0, D1)
    M6 = strassen(C0 - A0, A1 + B1)
    M7 = strassen(B0 - D0, C1 + D1)

    Z1 = M1 + M4 - M5 + M7
    Z2 = M3 + M5
    Z3 = M2 + M4
    Z4 = M1 - M2 + M3 + M6

    upper_left = np.vstack((np.hstack((Z1, Z2)), np.hstack((Z3, Z4))))
    return upper_left