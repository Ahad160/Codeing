#include<stdio.h>

    int main(){
    char print[]="Raiden";
    char *ptr = print;
    
    while(*ptr!='\0'){
    printf("%c",*ptr);
    *ptr++;
    }
    return 0;
}