#include<stdio.h>

    int main(){
    float tax;

    printf("Enter Youer income\n");
    scanf("%f",&tax);
     
     if(tax<250000)
    {
       printf("They are no tax below 250000\n");
    }

     if((tax>=250000)  && (tax<=500000))
     {
       printf("Youer income with (5%) tax is %f\n",0.05*(tax-250000));
    }

    if((tax>=500000) && (tax<=1000000))
    {
       printf("Youer income with (20%) tax is %f\n",0.20*(tax-500000));
    }

    if(tax>1000000)
    {
       printf("Youer income with (30%) tax is %f\n",0.30*(tax-3000000));
    }

    return 0;
}