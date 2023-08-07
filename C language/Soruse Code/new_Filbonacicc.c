#include <stdio.h>

int main() {
    int n, a = 0, b = 1, c;

    printf("Enter a positive number: ");
    scanf("%d", &n);

    printf("First %d Fibonacci numbers:\n", n);

    for (int i = 0; i < n; i++) {
        printf("%d\n", a);
        c = a + b;
        a = b;
        b = c;
    }

    return 0;
}

a="raiden"

print("my name is",a,'and i am good')