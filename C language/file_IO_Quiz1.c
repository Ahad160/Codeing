#include<stdio.h>

int main(){
     int num;
    FILE *ptr;
    ptr = fopen("simple3.txt","r");
    if(ptr == NULL){
        printf("This file does not exist\n");
    }

    else{
    fscanf(ptr,"%d",&num);
    fclose(ptr);

    printf("The value in num is %d\n",num);
    }
    return 0;
}