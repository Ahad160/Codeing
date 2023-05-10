#include<stdio.h>

    int main(){
    
    int user_input;
    int b;

    printf("Enter number\n");
    scanf("%d",&user_input);
    
    switch (user_input)
    {
    case 1:
        printf("hello\n");
        break;
    
    default:
          printf("bye\n");
        break;
    }
    return 0;
}