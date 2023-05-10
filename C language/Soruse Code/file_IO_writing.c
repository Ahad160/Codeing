#include<stdio.h>

int main(){
 int num=75;
    FILE *ptr;
    ptr =fopen("txt1.txt","w");
    fprintf(ptr,"The value in txt1 is %d\n",num);
    fclose(ptr);
    return 0;
}