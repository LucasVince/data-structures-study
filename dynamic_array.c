#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int maxSize;
    int logicSize;
    int * array;
    int overflowPercentage;
    int underflowPercentage;
} DynamicArray;

DynamicArray createArray(int size, int over, int under);
void printArray(DynamicArray * dArr);
void append(DynamicArray * dArr, int val);
int pop(DynamicArray * dArr);

int main() {
    DynamicArray dArr = createArray(10, 90, 25);

    return 0;
}

DynamicArray createArray(int size, int over, int under) {
    DynamicArray dArr;
    
    dArr.maxSize = size;
    dArr.logicSize = 0;
    dArr.overflowPercentage = over;
    dArr.underflowPercentage = under;
    
    dArr.array = malloc(size*sizeof(int));
    
    return dArr;
}

void append(DynamicArray * dArr, int val) {
    dArr->array[dArr->logicSize] = val;
    dArr->logicSize++;
}

int pop(DynamicArray * dArr) {
    dArr->logicSize--;
    return dArr->array[dArr->logicSize];
}

void printArray(DynamicArray * dArr) {
    printf("{ ");

    for (int i = 0 ; i < dArr->logicSize ; i++) {
            printf("%d ", dArr->array[i]);
    }

    printf("}\n");
}