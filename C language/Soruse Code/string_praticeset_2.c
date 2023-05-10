#include<stdio.h>
#include<string.h>

int strlen2(char *st);
int main(){
    
    char st[]= "jaketheripper";
    int i = strlen2(st);

    printf("The length of the strings is %d\n",i);

    return 0;
}
int strlen2(char *st){
    char *ptr =st;
    int len=0;
    while(*ptr != '\0'){
        len++;
        ptr++;
    }
    return len;
}
