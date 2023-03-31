#include<stdio.h>
int swap(int *a,int *b);

    int main(){
    int a=5;
    int b=10;
    
    swap(&a ,&b);

    printf("the value of a is %d\n",a);

    printf("the value of b is %d\n",b);

    return 0;
}

int swap(int *a,int *b){

    int temp;

      temp=*a;
      *a=*b;
      *b=temp;

    return *a,*b;


}
