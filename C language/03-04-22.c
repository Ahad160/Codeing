#include<stdio.h>

    int main(){
        int collam =2;
        int row =2;

        int array[2][2];

        for(int i=0;i<collam;i++){
            for(int j=0;j<row;j++){
                printf("Enter value of %d collam in row of %d\n",i+1,j+1);
                scanf("%d",&array[i][j]);
            }
        }
        for(int i=0;i<collam;i++){
            for(int j=0;j<row;j++){
                printf("%d\n",array[i][j]);
            }
        }
 
    
   
      
    return 0;
}