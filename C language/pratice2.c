#include<stdio.h>

    int main(){
    
    int height;
    int radius;
    float pi=3.14;
     
     printf("Enter Youer radius\n");
     scanf("%d",&radius);

     printf("Enter Youer height\n");
     scanf("%d",&height);

     printf("The volume of this cylinde is %f\n",pi*radius*radius*height);


    return 0;
}