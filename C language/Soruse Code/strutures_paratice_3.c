#include<stdio.h>

struct complex{

    int real;
    int complex; 
};
void display(struct complex a){
        printf("The real number is %d\n",a.real);
        printf("The complex number is %d\n",a.complex);

    }


int main(){

    struct complex arr[5];

    for(int i=0;i<5;i++){
        printf("Enter the real number of %d\n",i+1);
        scanf("%d",&arr[i].real);
    
        printf("Enter the complex number%d\n",i+1);
        scanf("%d",&arr[i].complex);
    }
    
    for(int i=0;i<5;i++){
    display(arr[i]);
    }
    return 0;
}