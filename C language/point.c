#include<stdio.h>

    int main(){
    
    int mark;

    printf("Enter youer Mark\n");
    scanf("%d", &mark);

    if(mark<=32){

        printf("You fall \n");
    }
        
    else if(mark>=33 && mark<39){
    
        printf("You got D\n");
    }
    
    else if(mark>=40 && mark<49){
    
        printf("You got C\n");
    }

    else if(mark>=50 && mark<59){
    
        printf("You got B\n");
    }

    else if(mark>=60 && mark<69){
    
        printf("You got A-\n");
    }

    else if(mark>=70 && mark<79){
    
        printf("You got A\n");
    }

    else if(mark>=80 && mark<100){
    
        printf("You got A+\n");
    }

    return 0;
}