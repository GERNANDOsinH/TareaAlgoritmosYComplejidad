import numpy as np

def quickSort(arr):
    # Descripción: Algoritmo de ordenamiento QuickSort que sigue la enfoque de diseño dividir y vencer
    # que necesita(en esta caso) memoria extra.

    # Si el arreglo tiene a lo mucho un elemento, se devuelve el propio arreglo.
    if len(arr) <= 1: return arr

    # Se elige al primer elemento como pivote.
    p = arr[0]

    # Se inicializan los arreglos lower(menor que) y greater(mayor que).
    lower = np.array([])
    greater = np.array([])

    # Se guardan los elementos menores que el pivote en la lista lower, y los demas en greater.
    for i in range(1,len(arr)):
        if arr[i] < p:
            lower = np.concatenate((lower, np.array([arr[i]])))
        else:
            greater = np.concatenate((greater, np.array([arr[i]])))

    # Llamada recursiva.
    ret = np.concatenate((quickSort(lower), np.array([p])))
    ret = np.concatenate((ret, quickSort(greater)))
    return ret