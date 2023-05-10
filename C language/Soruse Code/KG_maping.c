#include<stdio.h>

    int main(){
    
    int a;
    
    printf("Enter the Taka Amount\n");
    scanf("%d",& a);

    printf("%d in 0.5KG is %d \n\n",a,a*50/100);

    printf("%d in 1KG is %d \n\n",a,a*1);

    printf("%d in 1.5KG is %d \n\n",a,a*150/100);

    printf("%d in 2KG is %d \n\n",a,a*2);


    return 0;
}