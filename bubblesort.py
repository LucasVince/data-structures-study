array = [9, 1, 6, 4, 2, 3, 5, 7, 8, 10, 0]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

bubble_sort(array)

print(array)
