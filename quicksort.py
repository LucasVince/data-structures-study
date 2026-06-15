array = [7, 2, 10, 0, 9, 1, 8, 3, 6, 4, 5]

def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1

            aux = arr[j]
            arr[j] = arr[i]
            arr[i] = aux

    i += 1

    aux = arr[end]
    arr[end] = arr[i]
    arr[i] = aux

    quick_sort(arr, start, i - 1)
    quick_sort(arr, i + 1, end)
