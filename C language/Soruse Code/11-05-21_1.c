#include<stdio.h>

int main(){

    char first;

    printf("Enter the alphabet\n");
    scanf("%c",&first);

    if(first=='a')
    printf("the number is 1\n");
    
    else if(first=='b')
    printf("the number is 2\n");

    else if(first=='c')
    printf("the number is 3\n");

    else if(first=='d')
    printf("the number is 4\n");

    else if(first=='e')
    printf("the number is 5\n");

    else if(first=='f')
    printf("the number is 6\n");

    else if(first=='g')
    printf("the number is 7\n");

    else if(first=='h')
    printf("the number is 8\n");

    else if(first=='i')
    printf("the number is 9\n");

    else if(first=='j')
    printf("the number is 10\n");

    else{
        printf("invalid alphabate");
    }

    return 0;
}