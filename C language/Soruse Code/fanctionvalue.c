#include<stdio.h>
 int value(int a ,int b);

    int main(){
       int c;
     c= value(3,5);
     printf("the value is %d\n",c);
    
    return 0;
}

int value(int a, int b){
    int result;
    result = a+b;
     return result;
}