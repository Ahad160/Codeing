#include<stdio.h>

int main(){
    int num;
    FILE *ptr;
    printf("Enter the number of table you want\n");
    scanf("%d",&num);
    
    ptr = fopen("simple.txt", "w");
       
    for(int i=0;i<10;i++){
        fprintf(ptr,"%dX%d = %d\n",num,i+1,num*(i+1));
    }
    fclose(ptr);

    printf("Successfully generated table of %d to table.txt\n", num);

    return 0;
}