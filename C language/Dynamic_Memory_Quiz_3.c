#include<stdio.h>
#include<stdlib.h>

int main(){
    int n;
    int *ptr;
    ptr=(int *)calloc(n,sizeof(int));

    printf("Enter the N\n");
    scanf("%d",&n);

    // for(int i=0;i<n;i++){
    //     printf("Enter value of %d Element\n",i+1);
    //     scanf("%d",&ptr[i]);
    // }

     for(int i=0;i<n;i++){
        printf("The value of %d Element is %d\n",i+1,ptr[i]);

    }
    
    

  
    return 0;
}