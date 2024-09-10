import numpy as np
import time
import matplotlib.pyplot as plt

from mulMatrix import multiplicar_matrices
from mul2Matrix import multiplicarMatrices
from strassen import strassen


def graficar(T0, T1, T2, size):
    plt.scatter(size, T0, label = "Tiempo Ejecución Algoritmo Cubico", color = 'blue')
    plt.scatter(size, T1, label = "Tiempo Ejecución Algoritmo Cubico Optimizado", color = 'red')
    plt.scatter(size, T2, label = "Tiempo Ejecución Algoritmo Strassen", color = 'green')

    plt.plot(size, T0, label="Línea recta (Algoritmo Cubico)", color='blue', linestyle='--')
    plt.plot(size, T1, label="Línea recta (Algoritmo Cubico Optimizado)", color='red', linestyle='--')
    plt.plot(size, T2, label="Línea recta (Algoritmo Strassen)", color='green', linestyle='--')

    plt.xlabel('Tamaño matriz')
    plt.ylabel('Tiempo de Ejecución[ms]')
    plt.title('Tiempo de Ejecución Algoritmos de Multiplicación de Matrices')
    plt.legend()

    plt.show()

pairMatrix = []

with open('matrixAlgoritms/testMatrix.bin', 'rb') as file:
    while True:
        try:
            matrix0 = np.load(file)
            matrix1 = np.load(file)
            pairMatrix.append((matrix0, matrix1))
        except EOFError:
            break

timeClasicCubic = []
timeCubic = []
timeStrassen = []
sizeDataSet = []

for M0, M1 in pairMatrix:
    sizeDataSet.append(len(M0))

    start = time.time()
    multiplicar_matrices(M0,M1)
    stop = time.time()

    timeClasicCubic.append(round(1000*(stop - start),3))
    

    start = time.time()
    multiplicarMatrices(M0,M1)
    stop = time.time()

    timeCubic.append(round(1000*(stop - start),3))
    
    start = time.time()
    strassen(M0,M1)
    stop = time.time()

    timeStrassen.append(round(1000*(stop - start),3))


graficar(timeClasicCubic,timeCubic,timeStrassen,sizeDataSet)