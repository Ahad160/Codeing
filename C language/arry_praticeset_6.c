#include<stdio.h>

void print(int *table ,int num,int n){
    printf("The Table of %d\n",num);
    
    for(int i=0;i<n;i++){
        table[i] = num*(i+1);
    }
     
    for(int i=0;i<n;i++){
       printf("%dX%d = %d\n",num,i+1,table[i]); 

    }  
    printf("*************************************************\n\n");
}

    int main(){
    int table[3][10];
    int u[3];
        
        for(int i=0;i<3;i++){
            printf("Enter number for table\n");
            scanf("%d",&u[i]);
        }
    
    print(table[0],u[0],10);
    print(table[1],u[1],10);
    print(table[2],u[2],10);

    return 0;
}