array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def selection_sort(arr):
    for i in range(len (arr)):
        min = arr[i]

        for j in range(i, len(arr)):
            if arr[j] < array[min]:
                min = j
        
        aux = arr[i]
        arr[i] = arr[min]
        arr[min] = aux

selection_sort(array)

print(array)
