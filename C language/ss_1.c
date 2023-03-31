#include <stdio.h>

int main()
{
    int radius;

    float pi;

    int height;

    printf("Enter the value of radius\n");
    scanf("%d", &radius);

    printf("Enter the value of Pi\n");
    scanf("%f", &pi);

    printf("The area of this circle is %f\n", pi * radius * radius);

    printf("Ente the height\n");
    scanf("%d", &height);

    printf("volume of this cylinder is %f\n", pi * radius * radius * height);

    return 0;
}