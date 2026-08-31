array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                aux = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = aux

insertion_sort(array)

print(array)
