#include<stdio.h>
#include<stdlib.h>

int main(){
    int *ptr;
    int *ptr2;
  ptr= (int *)malloc(600 *sizeof(int));

  for(int i=0;i<600;i++){
  ptr2= (int *)malloc(600 *sizeof(int));

    printf("Enter value of %d\n",i+1);
    scanf("%d",&ptr[i]);
    free(ptr);
  }

  for(int i=0;i<600;i++){
    printf("the value of %d element is %d\n",i+1,ptr[i]);
  }
    return 0;
}