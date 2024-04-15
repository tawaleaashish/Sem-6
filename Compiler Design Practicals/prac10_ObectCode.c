#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 100

// Function to generate object code from 3-address code
void generateObjectCode(char code[][MAX_LINE_LENGTH], int n, char objectCode[][MAX_LINE_LENGTH]) {
    for (int i = 0; i < n; i++) {
        char *line = code[i];
        char *delim = " ";
        char *token = strtok(line, delim);
        char objectLine[MAX_LINE_LENGTH] = "";

        while (token != NULL) {
            if (strcmp(token, "if") == 0) {
                strcat(objectLine, "JUMP ");
                token = strtok(NULL, delim); // Skip the condition
            } else if (strcmp(token, "goto") == 0) {
                strcat(objectLine, "JUMP ");
            } else if (strcmp(token, "end") == 0) {
                strcat(objectLine, "HALT");
            } else {
                strcat(objectLine, token);
            }

            strcat(objectLine, " ");
            token = strtok(NULL, delim);
        }

        strcpy(objectCode[i], objectLine);
    }
}

int main() {
    char code[][MAX_LINE_LENGTH] = {
        "temp = 0",
        "i = 0",
        "L1: if i >= n goto L6",
        "min_idx = i",
        "j = i + 1",
        "L2: if j >= n goto L4",
        "t1 = arr[j]",
        "t2 = arr[min_idx]",
        "if t1 >= t2 goto L3",
        "min_idx = j",
        "L3: j = j + 1",
        "goto L2",
        "L4: t3 = arr[i]",
        "t4 = arr[min_idx]",
        "if t3 == t4 goto L5",
        "t5 = arr[i]",
        "arr[i] = arr[min_idx]",
        "arr[min_idx] = t5",
        "L5: i = i + 1",
        "goto L1",
        "L6: end"
    };

    int n = sizeof(code) / sizeof(code[0]);
    char objectCode[n][MAX_LINE_LENGTH];
    generateObjectCode(code, n, objectCode);

    printf("\nObject code:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", objectCode[i]);
    }

    return 0;
}