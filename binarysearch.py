def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if target < arr[middle]:
            right = middle - 1
        elif target > arr[middle]:
            left = middle + 1
        else:
            return middle

    return -1
