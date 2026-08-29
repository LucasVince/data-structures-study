#include <cstdio>
#include <iostream>
#include <unordered_map> 
#include <unordered_set>
#include <algorithm>
#include <iterator>
#include <string>
#include <array>
#include <span>
#include <vector>

using namespace std;

vector<int> quickSort(vector<int> arr);
void printList(span<const int> arr);

int main() {
    vector<int> numbers = {64, 512, 2, 128, 1024, 16, 256, 1, 32, 8};

    printList(numbers);
    printf("\n");
    printList(quickSort(numbers));

    return 0;
}

void printList(span<const int> arr) {
    printf("{");
    for (int num : arr) {
        printf("%d ", num);
    }
    printf("}");
} 

vector<int> quickSort(vector<int> arr) {
    if (arr.size() <= 1) {
        return arr;
    } else {
        srand(time(NULL));
        int pivot = rand() % size(arr);

        vector<int> low;
        vector<int> equal;
        vector<int> high;

        for (int i = 0; i < arr.size() ; i++) {
            if (arr[i] < arr[pivot]) {
                low.push_back(arr[i]);
            } else if (arr[i] == arr[pivot]) {
                equal.push_back(arr[i]);
            } else {
                high.push_back(arr[i]);
            }
        }

        vector<int> low_sorted = quickSort(low);
        vector<int> high_sorted = quickSort(high);

        low_sorted.insert(
            low_sorted.end(),
            equal.begin(),
            equal.end()
        );
        
        low_sorted.insert(
            low_sorted.end(),
            high_sorted.begin(),
            high_sorted.end()
        );

        return low_sorted;
    }
}
