#include<stdio.h>

struct victor
{
    int x;
    int y;
};

struct victor value(struct victor a,struct victor b){
      
      struct victor result;

    result.x = a.x + b.x;
    result.y = a.y + b.y;

    return result; 
}


int main(){
    
    struct victor a,b,sum;

    a.x = 5;
    a.y = 6;

    b.x = 4;
    b.y = 9;

    sum= value(a,b);

    printf("The victor x is %d and y is %d\n",sum.x, sum.y);





    return 0;
}