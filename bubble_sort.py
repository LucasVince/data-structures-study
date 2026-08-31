array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

bubble_sort(array)

print(array)
