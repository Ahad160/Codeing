#include<stdio.h>

    int main(){
    
    int physic,cremesty,math;
    float total;

    printf("Enter Physic Marks\n");
    scanf("%d", &physic);

    printf("Enter cremesty Marks\n");
    scanf("%d", &cremesty);

    printf("Enter math Marks\n");
    scanf("%d", &math);

     total=(physic+cremesty+math)/3;

     if((total<40) || physic<33 || cremesty<33 || math<33)
     {
       printf("Youer pracentice is %f and you are faill\n",total);
     }
     else
      printf("Youer pracentice is %f and you are pass\n",total);

    return 0;
}