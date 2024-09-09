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
    # Descripción: Algoritmo que une dos arreglos de números.
    sorted_list = []
    i = j = 0

    # Ordenamiento mediante comparación de elementos.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list