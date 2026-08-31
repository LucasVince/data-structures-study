from random import randint

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
    
def quicksort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[randint(0, len(arr) - 1)]
        low = []
        high = []

        for i in arr:
            if i < pivot:
                low.append(i)
            elif i > pivot:
                high.append(i)

        return quicksort(low) + [pivot] + quicksort(high)
