array = [7, 2, 10, 0, 5, 9, 1, 8, 3, 6, 4]

def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    middle = len(arr) // 2

    left = arr[:middle]
    right = arr[middle:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, arr)

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
