#include<stdio.h>
#include<stdlib.h>

int main(){
    int *ptr;
    ptr=(int *)malloc(3*sizeof(int));

    for(int i=0;i<3;i++){
        printf("Enter value of %d Element\n",i+1);
        scanf("%d",&ptr[i]);
    }

     for(int i=0;i<3;i++){
        printf("The value of %d Element is %d\n",i+1,ptr[i]);

    }
    
    

  
    return 0;
}