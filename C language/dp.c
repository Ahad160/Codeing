#include<stdio.h>

void print(int *table ,int *num,int n){
    printf("The Table of %d\n",*num);
    
    for(int i=0;i<n;i++){
        *table = (*num)*(i+1);
    }
     
    for(int i=0;i<n;i++){
       printf("%dX%d = %d\n",*num,i+1,*table); 

    }  
    printf("*************************************************\n\n");
}

    int main(){
    
    int m,n;
    int u;
    
            printf("Enter the size of row table\n");
            scanf("%d",&m);
        
        
           // printf("Enter the size of collam table\n");
           // scanf("%d",&n);
        
        
        for(int i=0;i<m;i++){
            printf("Enter number for table\n");
            scanf("%d",&u);
        }
    for(int i=0;i<m;i++){
    print(&m,&u,10);
    //print(table[1],u[1],10);
    //print(table[2],u[2],10);
    }
    return 0;
}