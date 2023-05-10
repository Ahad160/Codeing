#include <stdio.h>

int main()
{
    float celsius;

    printf("Enter ther value of celsius\n");
    scanf("%f", &celsius);

    printf("The value of celsius to temparecer is %f\n",celsius * 9 / 5 + 32);

    return 0;
}