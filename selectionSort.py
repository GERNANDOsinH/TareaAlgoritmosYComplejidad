def selectionSort(arr):
    for i in range(0,len(arr)):
        m = 0
        for j in range(0,len(arr)-i):
            if (arr[m] < arr[j]):
                m = j
        aux = arr[len(arr)-1 - i]
        arr[len(arr)-1 - i] = arr[m]
        arr[m] = aux
        arr
    return arr