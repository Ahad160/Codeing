#include<stdio.h>

    int main(){
    
    char n[10];
    char str[] = {'H', 'a', 'r', 'r', 'y', '\0'};
    //char str[] ={'r','a','w','\0'};

    printf("%c\n",str);
    printf("Enter youer name:");
    scanf("%s",n);
    
    printf("%c\n",str);
    printf("Youer name is %s",n);
    return 0;
}
