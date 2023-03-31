#include<stdio.h>
int main(){
int call(int *a ,int *b);
   
    int user1=5;
    int user2=10;
    
    call(&user1,&user2);
    printf("the value after change by call by refacence %d and %d\n",user1,user2);

    
}
int call(int *a ,int *b){
    *a=50;
    *b=410;
    
    return *a,*b;
}
