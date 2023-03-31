#include<stdio.h>

    int main(){
    int arr[10];
    int *ptr=&arr[0];
   ptr =ptr+8;

   if(ptr==&arr[8]){
       printf("yes\n");
   }
   else{
       printf("no");
   }
    return 0;
}