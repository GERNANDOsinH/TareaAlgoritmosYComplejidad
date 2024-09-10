def selectionSort(arr):
    # Descripción: Algoritmo de ordenamiento selectionSort que ordena los elementos de un arreglo de entrada.
    for i in range(0,len(arr)):
        m = 0
        # Bucle que compara los elementos para encontrar al menor
        for j in range(0,len(arr)-i):
            if (arr[m] < arr[j]):
                m = j
        # Se hace el intercambio de elementos.
        aux = arr[len(arr)-1 - i]
        arr[len(arr)-1 - i] = arr[m]
        arr[m] = aux
    return arr