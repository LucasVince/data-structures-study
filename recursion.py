array = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

def factorial(num):
    if num <= 1:
        return 1
    
    return num * factorial(num - 1)


def power(base, expo):
    if expo <= 1:
        return base

    return base * power(base, expo - 1)


def recursive_binary_search(arr, target):
    middle = (len(arr) // 2)

    if target < arr[middle]:
        return recursive_binary_search(arr[:middle + 1], target)
    elif target > arr[middle]:
        return recursive_binary_search(arr[middle - 1:], target)
    else:
        return middle


print(factorial(5))
print(power(2, 3))
print(recursive_binary_search(array, 16))
