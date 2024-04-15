#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 100

// Function to generate 3-address code for selection sort
void generateSelectionSortCode(int arr[], int n, char code[][MAX_LINE_LENGTH], int *codeIndex) {
    // Initialize code index
    *codeIndex = 0;

    // Declare temporary variables
    sprintf(code[*codeIndex], "temp = 0");
    (*codeIndex)++;
    sprintf(code[*codeIndex], "i = 0");
    (*codeIndex)++;
    sprintf(code[*codeIndex], "loop L1:");
    (*codeIndex)++;

    // Loop for selection sort
    for (int i = 0; i < n - 1; i++) {
        sprintf(code[*codeIndex], "if i >= %d goto L6", n);
        (*codeIndex)++;
        sprintf(code[*codeIndex], "min_idx = i");
        (*codeIndex)++;

        for (int j = i + 1; j < n; j++) {
            sprintf(code[*codeIndex], "t1 = arr[%d]", j);
            (*codeIndex)++;
            sprintf(code[*codeIndex], "t2 = arr[min_idx]");
            (*codeIndex)++;
            sprintf(code[*codeIndex], "if t1 >= t2 goto L3");
            (*codeIndex)++;
            sprintf(code[*codeIndex], "min_idx = %d", j);
            (*codeIndex)++;
            sprintf(code[*codeIndex], "L3:");
            (*codeIndex)++;
        }

        sprintf(code[*codeIndex], "t3 = arr[i]");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "t4 = arr[min_idx]");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "if t3 == t4 goto L5");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "t5 = arr[i]");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "arr[i] = arr[min_idx]");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "arr[min_idx] = t5");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "L5:");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "i = i + 1");
        (*codeIndex)++;
        sprintf(code[*codeIndex], "goto L1");
        (*codeIndex)++;
    }

    // End of program
    sprintf(code[*codeIndex], "L6: end");
    (*codeIndex)++;
}

int main() {
    int arr[] = {5, 3, 8, 1, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    char code[n * 10][MAX_LINE_LENGTH]; // Assuming a maximum of 10 lines of code per iteration
    int codeIndex;

    generateSelectionSortCode(arr, n, code, &codeIndex);

    printf("Generated 3-address code for Selection Sort:\n");
    for (int i = 0; i < codeIndex; i++) {
        printf("%s\n", code[i]);
    }

    return 0;
}