def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def multiplicarMatrices(A, B):
    B_transposed = transpose_matrix(B)

    n = len(A)
    m = len(B[0])
    p = len(B)

    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += A[i][k] * B_transposed[j][k]
    
    return result