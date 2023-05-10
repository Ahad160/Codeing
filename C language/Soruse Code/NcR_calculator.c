#include<stdio.h>


    int main(){
    int x,n1,n2; int fact1=1; int fact2=1; int fact3=1;
    
    int b;
    int final;
    printf("NCR Calculator\n");

    printf("Enter The number of N :");
    scanf("%d",&n1);
    printf("Enter The number of R :");
    scanf("%d",&n2);


    for(x=1;x<=n1;x++){

        fact1=fact1*x; 
    
    }

    for(x=1;x<=n2;x++){

        fact2=fact2*x; 
    
    }

    b=(n1-n2);

    for(x=1;x<=b;x++){

        fact3=fact3*x; 
    
    }
    final = fact1/ fact2 * (fact1-fact2);

    printf("Factorial of is: %d\n",final);

    return 0;
}

