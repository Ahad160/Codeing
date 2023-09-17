#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];

    // Input two strings
    printf("Enter the first string: ");
    scanf("%s", str1);

    printf("Enter the second string: ");
    scanf("%s", str2);

    // String concatenation
    strcat(str1, str2);
    printf("Concatenated string: %s\n", str1);

    // String length calculation
    int length = strlen(str1);
    printf("Length of the concatenated string: %d\n", length);

    // String comparison
    int compareResult = strcmp(str1, str2);
    if (compareResult == 0) {
        printf("The two strings are equal.\n");
    } else if (compareResult < 0) {
        printf("The first string is less than the second string.\n");
    } else {
        printf("The first string is greater than the second string.\n");
    }

    return 0;
}
// 