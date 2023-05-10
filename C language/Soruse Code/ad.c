#include<stdio.h>

int main(){
    
    int first;

    printf("which num pad number you want\n");
    scanf("%d",&first);

    if(first==1){

    printf("The alphabate is .,-` \n");
    }

    else if(first==2){
           printf("The alphabate is ABC\n");

    }
    
    else if(first==3){
           printf("The alphabate is DEF\n");

    }

    else if(first==4){
          printf("The alphabate is GHI\n");
    }

    else if(first==5){
            printf("The alphabate is JKL\n");
    }
    else{

        printf("Invalid num\n");
    }


    return 0;
}