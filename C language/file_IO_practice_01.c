#include<stdio.h>

int main(){
    int a,b,c;
    FILE *ptr;

    ptr =fopen("simple.txt","r");
    fscanf(ptr,"%d%d%d",&a,&b,&c);
    fclose(ptr);

    printf("The number of a ,b and c is %d %d %d\n",a,b,c);


    return 0;
}