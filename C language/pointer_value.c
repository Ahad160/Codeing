#include<stdio.h>
int value(int *a, int *b);
    int main(){
    int a=5;
    int b=5;

    value(&a,&b);

    printf("the value of a+b is %d\n",a+b);    
    return 0;
}

int value(int *a, int *b){
    int result;
    
    *a=25;
    *b=25;
    result= *a+*b;

    return result;

}
