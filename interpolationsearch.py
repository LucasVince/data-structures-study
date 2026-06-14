def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if target < arr[pos]:
            high = pos - 1
        elif target > arr[pos]:
            low = pos + 1
        else:
            return pos


    return -1
