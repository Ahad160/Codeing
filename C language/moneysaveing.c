#include<stdio.h>
int saveing(int n);
    int main(){

    int n;
    printf("Enter how many days money\n");
    scanf("%d",& n);
    printf("%d days money is %d\n",n,saveing(n));
    
    return 0;
}
int saveing(int n){
    
    if(n==1 || n==0){
        return 0;
    }
    int result;
    result= (n*(n+1))/2;
}