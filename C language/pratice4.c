#include<stdio.h>

    int main(){

    int principal;
    float rate;
    int time;
    
      printf("Enter principal\n");
      scanf("%d",&principal);

      printf("Enter rate% \n");
      scanf("%f",&rate);

      printf("Enter time/year\n");
      scanf("%d",&time);

      printf("Interest is %f\n",(principal*rate*time)/100);


    return 0;
}