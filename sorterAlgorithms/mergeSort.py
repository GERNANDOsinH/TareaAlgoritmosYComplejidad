import numpy as np

def merge_sort(arr):
    # Descripción: Algoritmo de ordenamiento QuickSort que ordena un arreglo de entrada mediante llamadas recursivas.
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Division del arreglo.
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llamada recursiva.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combinación de los elementos
    return merge(left_sorted, right_sorted)


def merge(left, right):
    # Descripción: Algoritmo que une dos arreglos de números usando numpy.
    sorted_array = np.empty(0, dtype=left.dtype)  # Crear un arreglo vacío con el mismo tipo de dato que `left`
    i = j = 0

    # Ordenamiento mediante comparación de elementos.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array = np.append(sorted_array, left[i])
            i += 1
        else:
            sorted_array = np.append(sorted_array, right[j])
            j += 1

    while i < len(left):
        sorted_array = np.append(sorted_array, left[i])
        i += 1
    while j < len(right):
        sorted_array = np.append(sorted_array, right[j])
        j += 1

    return sorted_array