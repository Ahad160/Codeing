#include<stdio.h>

int main(){
    FILE *ptr;
    ptr = fopen("txt1.txt","w");
    fputc('A',ptr);
    return 0;
}