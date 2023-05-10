#include<stdio.h>

int main(){
    char c ;
    FILE *ptr;
    ptr = fopen("txt1.txt","r");
    c = fgetc(ptr);
    printf("the character in txt1 is %c\n",c);
    printf("the character in txt1 is %c\n",fgetc(ptr));
    printf("the character in txt1 is %c\n",fgetc(ptr));


    return 0;
}