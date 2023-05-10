#include<stdio.h>

int possitive(int arr[]){
    int a=0;
    for(int i=0;i<10;i++){
        if(arr[i]%2==0){
          a++;
        }
    }
    printf("%d even number\n",a);
}


    int main(){
    int arr[]={1,2,3,4,5,6,7,8,9,10};

    possitive(arr);


    return 0;
}