#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main(void) {
    int TIM = 0;

    while (TRUE) {
        printf("%d\n", sec);
        sec++;
        Sleep(1000); // Sleep for 1 second (1000 milliseconds)
        if (sec == 120) {
            break;
        }
    }

    return 0;
}
