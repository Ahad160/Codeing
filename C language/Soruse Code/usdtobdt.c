#include<stdio.h>
int rate(int *a);

    int main(){

    int u;
    
    printf("USD = BDT //Rate= 86.56\n");
    printf("Enter USD amount\n");
    scanf("%d",&u);
     
    rate(&u);

    printf( "USD To BDT is %d",u);
    return 0;
}
int rate(int *a){
    *a=(*a*86.56);

    return *a;

}
