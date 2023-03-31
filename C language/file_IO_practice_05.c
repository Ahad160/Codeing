#include<stdio.h>

int main(){
    int num;
    FILE *ptr;
    ptr =fopen("simple.txt","r");
    fscanf(ptr,"%d",&num);
    ptr =fopen("simple.txt","w");
    fprintf(ptr,"%d\n",num*2);
    return 0;
}