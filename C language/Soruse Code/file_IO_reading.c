#include<stdio.h>

int main(){
    int num;
    FILE *ptr;
    ptr = fopen("simple2.txt","r");
    fscanf(ptr,"%d",&num);
    fclose(ptr);

    printf("The value in num is %d\n",num);
    return 0;
    
}