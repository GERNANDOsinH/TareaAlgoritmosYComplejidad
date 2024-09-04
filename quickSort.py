def quickSort(arr):
    if len(arr) == 0: return []
    p = arr[0]
    lower = []
    upper = []
    for i in range(1,len(arr)):
        if arr[i] < p:
            lower.append(arr[i])
        else:
            upper.append(arr[i])
    return (quickSort(lower) + [p] + quickSort(upper))