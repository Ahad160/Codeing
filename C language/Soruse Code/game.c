#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    
    int number;
    int user;
    int attemps=1;
    
    srand(time(0));
    number= rand()%100+1;
    
    do{
    printf("Guess the number between (1-100)\n");
    scanf("%d",&user);

     if(user>number){
         printf("Enter a Lower number\n");
     }
    
     else if(user<number){
        printf("Enter a higher number\n");
     }
    
     else{
        printf("You Guess the number is %d attemps\n",attemps);
     }
     attemps++;
    
    }while(user!=number);

    return 0;
}
 if("how to help a coder to code in begener")