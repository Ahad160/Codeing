#include<stdio.h>

int main(){
    int a;
    int b1,b2;

    printf("Simple calculator\n");

    printf("1.(+)\n2.(-)\n3.(*)\n4.(/)\n");
    scanf("%d",&a);

    if(a==1){
        printf("Enter the first number to (+)\n");
        scanf("%d",&b1);

        printf("Enter the secend number to (+)\n");
        scanf("%d",&b2);

        printf("Result %d\n",b1+b2); 
    
    return 0;
    }
    else if(a==2){
        printf("Enter the first number to (-)\n");
        scanf("%d",&b1);

        printf("Enter the secend number to (-)\n");
        scanf("%d",&b2);

        printf("Result%d\n",b1-b2);

    return 0;
    }
    else if(a==3){
        printf("Enter the first number to (*)\n");
        scanf("%d",&b1);

        printf("Enter the secend number to (*)\n");
        scanf("%d",&b2);

        printf("Result %d\n",b1*b2);

    return 0;
    }
    else if(a==4){
        printf("Enter the first number to (/)\n");
        scanf("%d",&b1);

        printf("Enter the secend number to (/)\n");
        scanf("%d",&b2);

        printf("Result %d\n",b1/b2);
         
    return 0;
    }

  
      
    return 0;
}