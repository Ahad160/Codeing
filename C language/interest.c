#include<stdio.h>

int main(){

    int prinicipal;

    int rate;

    int year;

    printf("Enter the Prinicipal\n");
    scanf("%d", &prinicipal);

    printf("Enter the rate\n");
    scanf("%d", &rate);
    
    printf("Enter the year\n");
    scanf("%d", &year);

    printf("The value of simple intersest is %d\n", prinicipal*rate*year/100);

    return 0;
}