#include <stdio.h>

int binary_search(const int arr[], int size, int target);

int main(void) {
    int numbers[] = {
        1, 2, 4, 8, 16,
        32, 64, 128, 256, 512
    };

    int size = sizeof(numbers) / sizeof(numbers[0]);

    int target = 64;

    int result = binary_search(numbers, size, target);

    if (result != -1) {
        printf(
            "Elemento %d encontrado no indice %d\n",
            target,
            result
        );
    } else {
        printf(
            "Elemento %d nao foi encontrado\n",
            target
        );
    }

    return 0;
}

int binary_search(const int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        }

        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}
