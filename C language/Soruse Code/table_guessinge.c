#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int main(){
    int plus;
    int number1;
    int number2;
    int user;
     for(int i;i>1;i++){

    srand(time(0));
    number1= rand()%9+1;

    srand(time(0));
    number2= rand()%10+1;
  
    
    printf("Table\n");
    printf("%dX%d\n\n",number1,number2);

    scanf("%d",&user);
    plus=number1*number2;
    
  
    if(user==plus){
        printf("right\n\n\n");
    }

    else
    {
        printf("wrong\n\n");
        printf("%dX%d=%d\n\n\n",number1,number2,plus);
    }
     }   

    return 0;
}



