import numpy as np
import time
import matplotlib.pyplot as plt

from selectionSort import selectionSort
from quickSort import quickSort
from mergeSort import merge_sort

def graficar(T0, T1, T2, T3, size):
    plt.scatter(size, T0, label = "Tiempo Ejecución Funcion Implementada", color = 'blue')
    plt.scatter(size, T1, label = "Tiempo Ejecución Algoritmo Selection Sort", color = 'red')
    plt.scatter(size, T2, label = "Tiempo Ejecución Algoritmo Quick Sort", color = 'green')
    plt.scatter(size, T3, label = "Tiempo Ejecución Algoritmo Merge Sort", color = 'pink')

    plt.xlabel('Tamaño arreglo')
    plt.ylabel('Tiempo de Ejecución[ms]')
    plt.title('Tiempo de Ejecución Algoritmos de Ordenamiento')
    plt.legend()

    plt.show()

def graficar1(T0, T1, T2, T3):
    N = 2
    bar_width = 0.2
    indices = np.arange(N)
    plt.bar(indices, T0, bar_width, label='Sort implementado en Numpy')
    plt.bar(indices + bar_width, T1, bar_width, label='SelectionSort')
    plt.bar(indices + 2 * bar_width, T2, bar_width, label='QuickSort')
    plt.bar(indices + 3 * bar_width, T3, bar_width, label='MergeSort')

    # Poner las etiquetas de las categorías centradas
    plt.xticks(indices + bar_width * 1.5, ["Ordenado Ascendente", "Aleatorio"])

    # Añadir una leyenda
    plt.legend()

    # Mostrar la gráfica
    plt.show()

staticArrays = []
with open('sorterAlgorithms/testSorterStatic.bin', 'rb') as file:
    while True:
        try:
            array = np.load(file)
            staticArrays.append(array)
        except EOFError:
            break

arreglos = []
with open('sorterAlgorithms/testSorter.bin', 'rb') as file:
    while True:
        try:
            array = np.load(file)
            arreglos.append(array)
        except EOFError:
            break

nativeAlgorithmTime = []
selSortTime = []
quickSortTime = []
mergeSortTime = []

for array in staticArrays:
    start = time.time()
    np.sort(array)
    stop = time.time()
    nativeAlgorithmTime.append(stop - start)

    start = time.time()
    selectionSort(array)
    stop = time.time()
    selSortTime.append(stop - start)

    start = time.time()
    quickSort(array)
    stop = time.time()
    quickSortTime.append(stop - start)

    start = time.time()
    merge_sort(array)
    stop = time.time()
    mergeSortTime.append(stop - start)


graficar1(nativeAlgorithmTime,selSortTime,quickSortTime,mergeSortTime)


sizes = []
nativeAlgorithmTime = []
selSortTime = []
quickSortTime = []
mergeSortTime = []


for array in arreglos:
    size = len(array)
    sizes.append(size)

    start = time.time()
    np.sort(array)
    stop = time.time()
    nativeAlgorithmTime.append(round(1000*(stop - start),3))

    start = time.time()
    selectionSort(array)
    stop = time.time()
    selSortTime.append(round(1000*(stop - start),3))

    start = time.time()
    quickSort(array)
    stop = time.time()
    quickSortTime.append(round(1000*(stop - start),3))

    start = time.time()
    merge_sort(array)
    stop = time.time()
    mergeSortTime.append(round(1000*(stop - start),3))

graficar(nativeAlgorithmTime,selSortTime,quickSortTime,mergeSortTime,sizes)