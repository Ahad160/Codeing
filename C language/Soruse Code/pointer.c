#include<stdio.h>

    int main(){
    int i=25;
    int *j =&i;
    int **k =&j;


    printf("the value of i is %d\n",i);

    printf("the address of i is %u\n",&i);

    printf("the value of j is %d\n",*j);

    printf("the adress of i in j is %u\n",j);

    printf("the address of j is %u\n",&j);

    printf("the value of j in k is %d\n",**k);

    printf("the value of i is %u\n",**(&k));


    printf("the address of k is %u\n",&k);



    
    // printf("the adrees of k is %u\n",**(&k));
    return 0;
}