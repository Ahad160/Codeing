#include<stdio.h>

    int main(){
    int a=85;
    int *b=&a;

    printf("the adress of a is %u\n",b);

    b++;
    printf("the adress of a afte a++ is %u\n",b);
    return 0;
}