#include<stdio.h>
#include<stdlib.h>

int main(){
    float *ptr;
    ptr=(float *)malloc(3*sizeof(float));

    for(int i=0;i<3;i++){
        printf("Enter value of %d Element\n",i+1);
        scanf("%f",&ptr[i]);
    }

     for(int i=0;i<3;i++){
        printf("The value of %d Element is %f\n",i+1,ptr[i]);

    }
    
    

  
    return 0;
}