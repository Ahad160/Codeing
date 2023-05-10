#include<stdio.h>

int main(){
    char c;
    FILE *ptr1;
    FILE *ptr2;

    ptr1 =fopen("simple.txt","r");
    ptr2 =fopen("simple2.txt","w");

    c=fgetc(ptr1);

    while(c != EOF){
        fputc(c,ptr2);
    c=fgetc(ptr1);
        
    }
    return 0;
}