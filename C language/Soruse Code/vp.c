#include<stdio.h>

int main(){

    char first;

    printf("Enter which value you want\n");
    scanf("%c"), &first;

    if(first==1){
    printf("The value is 1\n");
    }
    else if(first=='b'){
    printf("The value is 2\n");
    }
    else if(first=='c'){
    printf("The value is 3\n");
    }
    else if(first=='d'){
    printf("The value is 4\n");
    }
    else if(first=='e'){
    printf("The value is 5\n");
    }
    else{
        printf("Invalid number");
    }

    return 0;
}