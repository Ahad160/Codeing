#include<stdio.h>
#include<string.h>

struct data
{
    int code;
    float salary;
    char name[10];
};

int main(){
  
    struct data coder[100];

    coder[0].code=100;
    coder[0].salary=54.514;
    strcpy(coder[0].name,"Raiden");

    printf("%d\n",coder[0].code);
    printf("%f\n",coder[0].salary);
    printf("%s\n",coder[0].name);
    


        
    return 0;
}