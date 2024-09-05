import random

def newArr(maxLeng, minLeng, maxTerm, minTerm):
    n = random.randint(minLeng, maxLeng)
    arr = [0]*n
    for i in range(0,n):
        arr[i] = random.uniform(minTerm, maxTerm)
    return arr

def newMatrix(maxSize, minSize, maxTerm, minTerm):
    n = n = random.randint(minSize, maxSize)
    matrix = [[0]*n]*n
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = random.uniform(minTerm, maxTerm)
    return matrix

