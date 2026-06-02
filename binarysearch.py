array = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

def binary_search(arr, target):
    middle = (len(arr) // 2)

    if target < arr[middle]:
        binary_search(arr[:middle + 1], target)
    elif target > arr[middle]:
        binary_search(arr[middle - 1:], target)
    else:
        return middle

print(binary_search(array, 16))